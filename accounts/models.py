import uuid
import pytz
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from core.enums import RoleEnum

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

       
class StudyBuddyGeneralInfo(models.Model):
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







