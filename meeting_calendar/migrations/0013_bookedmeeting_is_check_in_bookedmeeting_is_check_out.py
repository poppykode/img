# Generated by Django 5.0.3 on 2024-08-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_calendar', '0012_avaliability_is_disabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedmeeting',
            name='is_check_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookedmeeting',
            name='is_check_out',
            field=models.BooleanField(default=False),
        ),
    ]
