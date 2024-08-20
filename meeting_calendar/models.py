import datetime
from datetime import datetime as dt, timedelta
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from core.enums import DayEnum

User = settings.AUTH_USER_MODEL

class BookedMeetingManager(models.Manager):
    def for_user(self, user):
        return self.filter(models.Q(requester=user) | models.Q(requested=user))
    
    def quick_meetings(self,user):
        return self.filter(requested = None).exclude(requester=user).exclude(booking_date__lt = datetime.date.today()).exclude(cancelled = True)
    
    def to_check_in(self,minutes):
        now = dt.now()
        threshhold = now + timedelta(minutes=minutes)
        print(f"Now: {now}")
        print(f"Threshhold: {threshhold}") 
        return BookedMeeting.objects.filter(
            booking_date=now.date(),
            availability__start_time__lte=threshhold,
            availability__start_time__gte=now,
            accepted=True,
            is_check_in = False,
            is_check_out = False
        )
    
    def to_check_out(self,minutes): 
        now = dt.now()
        threshhold = now - timedelta(minutes= minutes)     
        return BookedMeeting.objects.filter(
            booking_date= now,
            availability__end_time__lte=threshhold,
            accepted=True,
            is_check_in = True,
            is_check_out = False
        )
    
  
# Create your models here.
class BookedMeeting (models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE, related_name="requester")
    requested = models.ForeignKey(User,on_delete=models.CASCADE, related_name="requested", blank=True,null=True)
    availability = models.ForeignKey('Avaliability', on_delete=models.CASCADE, related_name='booked_meeting_availability')
    notes = models.TextField(blank=True, null=True)
    booking_date = models.DateField()
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    is_check_in = models.BooleanField(default=False)
    is_check_out = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BookedMeetingManager()

    def get_absolute_url(self):
        return reverse('meeting_calendar:meeting_detail', kwargs={'meeting_id': self.pk})

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
    is_temp = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
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

