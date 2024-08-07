# Generated by Django 5.0.3 on 2024-05-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_alter_subscription_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('successfull', 'Successfull'), ('cancelled', 'Cancelled'), ('failed', 'Failed'), ('processing', 'Processing')], default='processing', max_length=20),
        ),
    ]
