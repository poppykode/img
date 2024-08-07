# Generated by Django 5.0.3 on 2024-07-10 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_calendar', '0005_rename_is_check_out_meetingcheckinandout_is_checked_out'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedmeeting',
            old_name='attended',
            new_name='accepted',
        ),
        migrations.AddField(
            model_name='bookedmeeting',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
