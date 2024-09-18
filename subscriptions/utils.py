import stripe, logging
from decimal import Decimal
from datetime import date
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404
from django.conf import settings

from core.utils import get_current_datetime,convert_date_to_string
from subscriptions.task import send_notification_mail
from .models import SubscriptionProduct, Subscription
from accounts.models import User

from core.enums import CurrencyEnum, IntervalEnum, StatusEnum

SECRET_KEY = settings.STRIPE_SECRET_KEY

stripe.api_key = SECRET_KEY
logging.basicConfig(filename="subscription.log", level=logging.INFO)


def get_stripe_price_in_cents(price) -> int:
    stripe_price = int(price * 100)
    return stripe_price


def create_stripe(product_name: str, price) -> tuple[str, str, int]:
    if product_name:
        try:
            stripe_product = stripe.Product.create(name=product_name)
            stripe_product_id = stripe_product.id
            stripe_price_in_cents = get_stripe_price_in_cents(price)
            stripe_price = stripe.Price.create(
                product=stripe_product_id,
                unit_amount=stripe_price_in_cents,
                currency=CurrencyEnum.GBP.value,
            )
            stripe_price_id = stripe_price.id
            return stripe_product_id, stripe_price_id, stripe_price_in_cents

        except stripe.error.StripeError as e:
            print(f"Stripe Error : {e}")
            raise


def edit_stripe(obj, product_name: str, price: Decimal):
    try:
        modified_stripe_price_id = ""
        stripe_product = stripe.Product.retrieve(obj.stripe_product_id)
        if not stripe_product.name == product_name:
            print("Price Modify")
            stripe.Product.modify(stripe_product.id, name=product_name)
        stripe_price = stripe.Price.retrieve(obj.stripe_price_id)
        current_price = get_stripe_price_in_cents(price)
        if not stripe_price.unit_amount == current_price:
            print("Price Modify")
            stripe.Price.modify(stripe_price.id, active=False)
            new_stripe_price = stripe.Price.create(
                product=stripe_product.id,
                unit_amount=current_price,
                currency=CurrencyEnum.GBP.value,
            )
            modified_stripe_price_id = new_stripe_price.id
        return modified_stripe_price_id
    except stripe.error.StripeError as e:
        print(f"Stripe Error : {e}")
        raise


def calculate_subscription_expiry_date(sub_id):
    sub_obj = get_object_or_404(SubscriptionProduct, id=sub_id)
    sub_date = date.today()
    interval_mapping = {
        IntervalEnum.MONTH.value: relativedelta(months=sub_obj.duration_period),
        IntervalEnum.YEAR.value: relativedelta(years=sub_obj.duration_period),
        IntervalEnum.DAY.value: relativedelta(days=sub_obj.duration_period),
    }
    try:
        date_to_be_added = interval_mapping[sub_obj.interval]
        expiry_date = sub_date + date_to_be_added
    except Exception as e:
        print(e)
        raise

    return expiry_date


def create_subscription(sub_obj, user_id, check_out_session_id):
    user_obj = get_object_or_404(User, id=user_id)
    subscription = Subscription.objects.create(
        user=user_obj,
        subscription_product=sub_obj,
        check_out_session_id=check_out_session_id,
    )
    logging.info(f"resp --->> {subscription.id}")
    return subscription


def successful_subscription(check_out_session_id, sub_id):
    sub_obj = get_object_or_404(Subscription, check_out_session_id=check_out_session_id)
    sub_obj.expiration_date = calculate_subscription_expiry_date(sub_id)
    sub_obj.is_active = True
    sub_obj.is_successfully = True
    sub_obj.status = StatusEnum.SUCCESSFULL.value
    sub_obj.save()
    return sub_obj


def unsuccessful_subscription(check_out_session_id):
    sub_obj = get_object_or_404(Subscription, check_out_session_id=check_out_session_id)
    sub_obj.status = StatusEnum.CANCELLED.value
    sub_obj.save()
    return sub_obj


def check_if_active_subscription(request):
    is_grayed_out = False
    is_subscribed = (
        Subscription.objects.filter(user=request.user).filter(is_active=True).exists()
    )
    if is_subscribed:
        is_grayed_out = True
    return is_grayed_out

def expire_subscriptions():
  today = date.today()
  subscriptions_to_expire = Subscription.objects.filter(
      expiration_date__lte=today, is_active=True
  )
  print(subscriptions_to_expire)
  if not subscriptions_to_expire:
      logging.info(f"{subscriptions_to_expire.count()} subscriptions expired on {get_current_datetime()}")
  else:
      logging.info(
          f"{subscriptions_to_expire.count()} subscriptions expired on {get_current_datetime()}"
      )
      email_list = get_email_list(subscriptions_to_expire)
      subscriptions_to_expire.update(is_active=False)  # Update subscriptions

      for email in email_list:
          package, expiry_date, to, subject = email["package"], email["expiry_date"], email["to"], email["subject"]
          message = f"Your {package} expired {expiry_date}."
          print(f"Triggering email notification for {to}")
          send_notification_mail.delay(to, message, subject)


def get_email_list(subscriptions_to_expire):
    emails = []
    for email_infor in subscriptions_to_expire:
        package = email_infor.subscription_product.title
        emails.append(
            {
                "to": email_infor.user.email,
                "package": package,
                "expiry_date": convert_date_to_string(email_infor.expiration_date),
                "subject": f"Subscription expiry for {package}",
            }
        )

    return emails
