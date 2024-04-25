from django.db import models

from core.enums import CandidateInquiryEnum as ci_enum

# Create your models here.

class FirstLevelStation(models.Model):
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]

class SecondLevelStation(models.Model):
    first_level_station = models.ForeignKey(FirstLevelStation,related_name='first_level_station', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]

class ThirdLevelStation(models.Model):
    second_level_station=models.ForeignKey(SecondLevelStation,related_name='second_level_station', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.second_level_station.first_level_station.title} -> {self.second_level_station.title} ->{self.title}"

    class Meta:
        ordering = ["-timestamp", ]


class CandidateInstruction(models.Model):
    class Inquiry(models.TextChoices):
        LOCATION = ci_enum.LOCATION.value
        PATIENT_INFO = ci_enum.PATIENT_INFO.value
        OTHER_PATIENT_INFO = ci_enum.OTHER_PATIENT_INFO.value
        ACTION_REQUIRED = ci_enum.ACTION_REQUIRED.value

    station = models.ForeignKey(ThirdLevelStation,related_name='candidate_station', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, choices=Inquiry.choices)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.station.title} - {self.heading}"

    class Meta:
        ordering = ["-timestamp", ]

