import stripe
from django.db import models
from django.conf import settings

from core.enums import CurrencyEnum, IntervalEnum, StatusEnum

SECRET_KEY = settings.STRIPE_SECRET_KEY
USER = settings.AUTH_USER_MODEL

stripe.api_key = SECRET_KEY

# Create your models here.
# Sorry it’s £49.99 for 1 month and £79.99 for 3 months and £99.99 for 6 months access

class SubscriptionProduct(models.Model):
    class Interval(models.TextChoices):
        MONTH = IntervalEnum.MONTH.value
        DAY = IntervalEnum.DAY.value
        YEAR = IntervalEnum.YEAR.value

    title = models.CharField(max_length=255)
    interval = models.CharField(max_length=255, choices=Interval.choices)
    currency = models.CharField(max_length=10,default= CurrencyEnum.GBP.value)
    is_active = models.BooleanField()
    stripe_product_id = models.CharField(max_length=255,blank=True)
    stripe_price_id = models.CharField(max_length=255,blank=True)
    duration_period = models.IntegerField(default=0)
    stripe_price = models.IntegerField(default=0,blank=True) #price *100
    price =models.DecimalField(default=0.0, max_digits=10,decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]

    # def save(self, *args, **kwargs):
        
    #     if self.price:
    #         self.stripe_price = int(self.price * 100)
    #     if self.title:
    #         stripe_product_obj = stripe.Product.create(name=self.title)
    #         self.stripe_product_id = stripe_product_obj.id
    #     if self.stripe_product_id:
    #         stripe_price_obj  = stripe.Price.create(
    #             product=self.stripe_product_id,
    #             unit_amount=self.stripe_price,
    #             currency= self.currency,
    #             )
    #         self.stripe_price_id = stripe_price_obj.id
    #     super().save(*args, **kwargs)

class Subscription(models.Model):
    class Status(models.TextChoices):
        SUCCESSFULL = StatusEnum.SUCCESSFULL.value
        CANCELLED = StatusEnum.CANCELLED.value
        FAILED = StatusEnum.FAILED.value
        PROCESSING = StatusEnum.PROCESSING.value
    user = models.ForeignKey(USER,related_name='user_subscription', on_delete=models.CASCADE)
    subscription_product = models.ForeignKey(SubscriptionProduct,related_name='user_subscription_product', on_delete=models.CASCADE)
    check_out_session_id = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_successfully = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices= Status.choices, default=Status.PROCESSING)
    expiration_date = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name

    class Meta:
        ordering = ["-timestamp", ]
        
