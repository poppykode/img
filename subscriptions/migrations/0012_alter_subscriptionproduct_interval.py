# Generated by Django 5.0.3 on 2024-05-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0011_alter_subscriptionproduct_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='interval',
            field=models.CharField(choices=[('Month', 'Month'), ('Day', 'Day'), ('Year', 'Year')], max_length=255),
        ),
    ]
