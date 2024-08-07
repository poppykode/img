# Generated by Django 5.0.3 on 2024-07-10 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_calendar', '0006_rename_attended_bookedmeeting_accepted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedmeeting',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='bookedmeeting',
            name='start_date',
        ),
        migrations.AddField(
            model_name='bookedmeeting',
            name='availability',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booked_meeting_availability', to='meeting_calendar.avaliability'),
            preserve_default=False,
        ),
    ]
