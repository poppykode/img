import stripe
from django.conf import settings

SECRET_KEY = settings.STRIPE_SECRET_KEY

stripe.api_key = SECRET_KEY


def product_sales_pipeline(product_name='Test', price_in_cents=1000):

    try:
        # Create the Stripe product
        stripe_product = stripe.Product.create(
            name=product_name
        )
        product_id = stripe_product.id

        # Create the Stripe price (in cents)
        stripe_price = stripe.Price.create(
            product=product_id,
            unit_amount=price_in_cents,
            currency="usd",
        )
        price_id = stripe_price.id

        # Create the Stripe checkout session
        base_url = 'http://127.0.0.1:8000'  # Replace with your actual base URL
        success_url = f'{base_url}/subscriptions/success/'
        cancel_url = f'{base_url}/subscriptions/cancel/'

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1
                }
            ],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url
        )

        return checkout_session.url

    except stripe.error.StripeError as e:
        # Handle Stripe errors appropriately (e.g., logging, error messages)
        print(f"Error creating Stripe session: {e}")
        raise

