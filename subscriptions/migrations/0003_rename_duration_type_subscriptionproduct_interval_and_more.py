# Generated by Django 5.0.3 on 2024-05-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_subscriptionproduct_stripe_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptionproduct',
            old_name='duration_type',
            new_name='interval',
        ),
        migrations.AddField(
            model_name='subscriptionproduct',
            name='stripe_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscriptionproduct',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
