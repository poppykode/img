from django.conf import settings
from django.db import models
from core.enums import DayEnum

User = settings.AUTH_USER_MODEL

class BookedMeetingManager(models.Manager):
    def for_user(self, user):
        return self.filter(models.Q(requester=user) | models.Q(requested=user))
    
# Create your models here.
class BookedMeeting (models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE, related_name="requester")
    requested = models.ForeignKey(User,on_delete=models.CASCADE, related_name="requested")
    availability = models.ForeignKey('Avaliability', on_delete=models.CASCADE, related_name='booked_meeting_availability')
    notes = models.TextField(blank=True, null=True)
    booking_date = models.DateField()
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BookedMeetingManager()

    def __str__(self):
        return self.requester.first_name

    class Meta:
        ordering = ["-timestamp", ]

class Avaliability (models.Model):
    class Day(models.TextChoices):
        MONDAY = DayEnum.MONDAY.value
        TUESDAY = DayEnum.TUESDAY.value
        WEDNESDAY = DayEnum.WEDNESDAY.value
        THURSDAY = DayEnum.THURSDAY.value
        FRIDAY = DayEnum.FRIDAY.value
        SATURDAY = DayEnum.SATURDAY.value
        SUNDAY = DayEnum.SUNDAY.value  
         
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_availability")
    day =models.CharField(max_length=12,choices=Day.choices)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.day} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}) - ID: {self.id}"

    class Meta:
        ordering = ["-timestamp", ]

class MeetingCheckInAndOut(models.Model):
    booked_meeting = models.ForeignKey(BookedMeeting,on_delete=models.CASCADE, related_name="booked_meeting_check_in_and_out")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_check_in_and_out')
    is_checked_in = models.BooleanField(default=False)
    is_checked_out = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ["-timestamp", ] 

