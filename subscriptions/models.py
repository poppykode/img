from django.db import models

# Create your models here.
# Sorry it’s £49.99 for 1 month and £79.99 for 3 months and £99.99 for 6 months access

class SubscriptionProduct(models.Model):
    class DurationType(models.TextChoices):
        MONTHS = 'Months'
        DAYS = 'Days'
        YEARS = 'Year'
    title = models.CharField(max_length=255)
    duration_type = models.CharField(max_length=255, choices=DurationType.choices)
    duration_period = models.IntegerField(default=0)
    price =models.FloatField(default=0.0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]
