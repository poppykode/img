# Generated by Django 5.0.3 on 2024-07-10 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_calendar', '0004_meetingcheckinandout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingcheckinandout',
            old_name='is_check_out',
            new_name='is_checked_out',
        ),
    ]
