import uuid
import pytz
from django.db.models import Avg, Count, Q
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from core.enums import RoleEnum
from review_ratings.models import ReviewRating
from meeting_calendar.models import BookedMeeting,MeetingCheckInAndOut


# Create your models here.
class User (AbstractUser):
    class Role(models.TextChoices):
        CANDIDATE = RoleEnum.CANDIDATE.value
        COACH = RoleEnum.COACH.value
        ADMIN = RoleEnum.ADMIN.value

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length = 100,choices = Role.choices, default = Role.ADMIN)

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() + ' | ' + str(self.email)

    class Meta:
        ordering = ["-date_joined", ]

    def averageReview(self):
        reviews = ReviewRating.objects.filter(user_rated=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(user_rated=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
    

    def meeting_attendance(self):
        meetings = MeetingCheckInAndOut.objects.filter(user=self).filter(is_checked_in = True).filter(is_checked_out = True).aggregate(count=Count('id'))
        count = 0
        if meetings['count'] is not None:
            count = int(meetings['count'])
        return count
    
    def reliability(self):
        number_of_meeting_accepted = BookedMeeting.objects.filter((Q(requester=self) | Q(requested=self)) & Q(accepted=True)).aggregate(count=Count('id'))
        meetings_attended = self.meeting_attendance()


        reliability_percentage = 0
        number_of_meeting_accepted_ = 0

        if number_of_meeting_accepted['count'] is not None:
            number_of_meeting_accepted_ = int(number_of_meeting_accepted['count'])


        if not number_of_meeting_accepted_ == 0 and not meetings_attended == 0:
            reliability_percentage = (meetings_attended / number_of_meeting_accepted_) * 100

        return reliability_percentage

       
class GeneralInfo(models.Model):
    GENDER=(('','select a gender'),
            ('male','Male'),
            ('female','Female'),
            ('diversity','Diversity')
            )
    user=models.OneToOneField(User,related_name='user_general_additional_info', on_delete=models.CASCADE)
    gender = models.CharField(max_length=10,choices=GENDER)
    time_zone = models.CharField(max_length=255,choices=[(x,x) for x in pytz.all_timezones_set])
    phone_number = models.CharField(max_length=255, null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class StudyBuddyAdditionalInfo(models.Model):
    user=models.OneToOneField(User,related_name='study_buddy_additional_info', on_delete=models.CASCADE)
    exam_date = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]


class SessionExpectationAndAvailabilityInfo(models.Model):
    user=models.OneToOneField(User,related_name='session_expectation_and_availability', on_delete=models.CASCADE)
    availability_and_session_expectation = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class CoachWorkExperience(models.Model):
    user=models.ForeignKey(User,related_name='user_work_experience', on_delete=models.CASCADE)
    name_of_hospital = models.CharField(max_length=255)
    country_of_hospital = models.CharField(max_length=255)
    position_at_the_hospital = models.CharField(max_length=255)
    period_from =models.DateField()
    period_to = models.DateField() 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class CoachEducation(models.Model):
    user=models.ForeignKey(User,related_name='user_education', on_delete=models.CASCADE)
    name_of_instutution = models.CharField(max_length=255)
    period_from =models.DateField()
    period_to = models.DateField() 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class CoachMotivation(models.Model):
    user=models.OneToOneField(User,related_name='user_motivation', on_delete=models.CASCADE)
    description = HTMLField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class CoachAdditionalInfo(models.Model):
    user=models.OneToOneField(User,related_name='user_coach_additional_info', on_delete=models.CASCADE)
    cv = models.FileField(upload_to='files')
    nhs_experience = models.CharField(max_length=255)
    rate = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]








