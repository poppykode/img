from decimal import Decimal
import stripe
from django.conf import settings

from core.enums import CurrencyEnum

SECRET_KEY = settings.STRIPE_SECRET_KEY

stripe.api_key = SECRET_KEY

def get_stripe_price_in_cents(price) -> int:
    stripe_price = int(price * 100)
    return stripe_price

def create_stripe(product_name: str, price)-> tuple[str, str, int]:
    if product_name:
        try:
            stripe_product = stripe.Product.create(
                name=product_name
            )
            stripe_product_id = stripe_product.id
            stripe_price_in_cents = get_stripe_price_in_cents(price)
            stripe_price = stripe.Price.create(
                product=stripe_product_id,
                unit_amount= stripe_price_in_cents,
                currency= CurrencyEnum.GBP.value,
            )
            stripe_price_id = stripe_price.id
            return stripe_product_id, stripe_price_id, stripe_price_in_cents

        except stripe.error.StripeError as e:
            print(f"Stripe Error : {e}")
            raise

def edit_stripe(obj, product_name: str, price: Decimal):
    try: 
        modified_stripe_price_id = ''
        stripe_product = stripe.Product.retrieve(obj.stripe_product_id)
        if not stripe_product.name == product_name:
            print('Price Modify')
            stripe.Product.modify(
                stripe_product.id,
                name = product_name
            )
        stripe_price = stripe.Price.retrieve(obj.stripe_price_id)
        current_price = get_stripe_price_in_cents(price)
        if not stripe_price.unit_amount == current_price:
            print('Price Modify')
            stripe.Price.modify(
               stripe_price.id,
                active  = False
            )
            new_stripe_price = stripe.Price.create(
                product=stripe_product.id,
                unit_amount= current_price,
                currency=CurrencyEnum.GBP.value
            )
            modified_stripe_price_id = new_stripe_price.id
        return modified_stripe_price_id
    except stripe.error.StripeError as e:
        print(f"Stripe Error : {e}")
        raise
def retrive_product():
    x = stripe.Product.retrieve('prod_Q9XI4n1AchnGPQ')
    print(x)

