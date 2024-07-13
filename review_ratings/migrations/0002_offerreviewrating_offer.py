# Generated by Django 5.0.3 on 2024-07-08 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
        ('review_ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerreviewrating',
            name='offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='offer_review', to='offers.offer'),
            preserve_default=False,
        ),
    ]