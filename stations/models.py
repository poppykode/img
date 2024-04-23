from django.db import models

# Create your models here.

class Station(models.Model):
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]

class StationCategory(models.Model):
    station=models.ForeignKey(Station,related_name='station_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]

class StationSubCategory(models.Model):
    station_sub_category=models.ForeignKey(StationCategory,related_name='station_sub_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]


