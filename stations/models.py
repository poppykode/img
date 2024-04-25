from django.db import models

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


# class CandidateInstruction(models.Model):
#     station = models.ForeignKey(ThirdLevelStation,related_name='candidate_station', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     updated = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#          return self.title

#     class Meta:
#         ordering = ["-timestamp", ]

