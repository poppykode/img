from django.db import models
from django_quill.fields import QuillField

from core.enums import CandidateInquiryEnum as ci_enum, ExaminerMarkSheetEnum as ems_enum, PatientDisclosureEnum as pd_enum

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
        WHERE_ARE_YOU = ci_enum.WHERE_ARE_YOU.value
        WHO_THE_PATIENT_IS = ci_enum.WHO_THE_PATIENT_IS.value
        OTHER_INFORMATION_ABOUT_THE_PATIENT = ci_enum.OTHER_INFORMATION_ABOUT_THE_PATIENT.value
        WHAT_YOU_MUST_DO = ci_enum.WHAT_YOU_MUST_DO.value

    station = models.ForeignKey(ThirdLevelStation,related_name='candidate_station', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, choices=Inquiry.choices)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.station.title} - {self.heading}"

    class Meta:
        ordering = ["timestamp", ]

class PatientInstruction(models.Model):
    class Disclosure(models.TextChoices):
        FREELY_DIVULGED_TO_DOCTOR = pd_enum.FREELY_DIVULGED_TO_DOCTOR.value
        DIVULGED_TO_DOCTOR_IF_ASKED = pd_enum.DIVULGED_TO_DOCTOR_IF_ASKED.value
        IDEAS_CONCERNS_AND_EXPECTATIONS = pd_enum.IDEAS_CONCERNS_AND_EXPECTATIONS.value
        
    station = models.ForeignKey(ThirdLevelStation,related_name='patient_station', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, choices=Disclosure.choices)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.station.title} - {self.heading}"

    class Meta:
        ordering = ["timestamp", ]


class ExaminerMarkSheet(models.Model):
    class Heading(models.TextChoices):
        DATA_GATHERING = ems_enum.DATA_GATHERING.value
        INTERPERSONAL_SKILLS = ems_enum.INTERPERSONAL_SKILLS.value
        MANAGEMENT = ems_enum.MANAGEMENT.value
        
    station = models.ForeignKey(ThirdLevelStation,related_name='examiner_mark_sheet', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, choices=Heading.choices)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.station.title} - {self.heading}"

    class Meta:
        ordering = ["timestamp", ]

class ExaminerMarkSheetAnswer(models.Model):    
    examiner_mark_sheet = models.ForeignKey(ExaminerMarkSheet,related_name='examiner_mark_sheet_answer', on_delete=models.CASCADE)
    answer = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.examiner_mark_sheet} - {self.answer}"

    class Meta:
        ordering = ["timestamp", ]


class StationApproach(models.Model):
    station = models.ForeignKey(ThirdLevelStation,related_name='station_approach', on_delete=models.CASCADE)   
    learning_points = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.station.title} - {self.learning_points}"

    class Meta:
        ordering = ["timestamp", ]

class StationApproachLink(models.Model):
    station_approach = models.ForeignKey(StationApproach,related_name='station_approach_link', on_delete=models.CASCADE)   
    link =models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.station_approach.station.title} - {self.link}"

    class Meta:
        ordering = ["timestamp", ]




    

