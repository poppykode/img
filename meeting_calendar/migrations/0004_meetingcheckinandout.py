# Generated by Django 5.0.3 on 2024-07-10 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_calendar', '0003_remove_avaliability_attended'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingCheckInAndOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_checked_in', models.BooleanField(default=False)),
                ('is_check_out', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('booked_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_meeting_check_in_and_out', to='meeting_calendar.bookedmeeting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_check_in_and_out', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
