from decimal import Decimal
import stripe
from django.conf import settings

SECRET_KEY = settings.STRIPE_SECRET_KEY

stripe.api_key = SECRET_KEY

def get_stripe_price_in_cents(price:float) -> int:
    stripe_price = int(price * 100)
    return stripe_price

def create_stripe(product_name: str, currency: str, price)-> tuple[str, str, int]:
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
                currency=currency,
            )
            stripe_price_id = stripe_price.id
            return stripe_product_id, stripe_price_id, stripe_price_in_cents

        except stripe.error.StripeError as e:
            print(f"Stripe Error : {e}")
            raise

def edit_stripe(obj, product_name: str, currency: str, price: Decimal):
    try:
        if obj.title != product_name:
            print('Price Modify')
            stripe.Product.modify(
                obj.stripe_product_id,
                name = product_name
            )
        if obj.price != price or obj.currency != currency :
            print('Price Modify')
            stripe.Price.modify(
                obj.stripe_price_id,
                price  =  get_stripe_price_in_cents(price),
                currency = currency
            )
    except stripe.error.StripeError as e:
        print(f"Stripe Error : {e}")
        raise


