# Generated by Django 5.0.3 on 2024-07-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_calendar', '0011_alter_bookedmeeting_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliability',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
