# Generated by Django 5.0.3 on 2024-05-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionproduct',
            name='stripe_product_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]