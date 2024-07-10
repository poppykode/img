from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


User = settings.AUTH_USER_MODEL

# Create your models here.

class ReviewRating(models.Model):
    user_rating = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_rating_review')
    user_rated = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_rated_review')
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_rating.first_name
    
    class Meta:
        ordering = ["timestamp",]

class AvgRating(models.Model):
    user_avg_rating = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_avg_rating')
    avg_rating = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_avg_rating.first_name
    
    class Meta:
        ordering = ["timestamp",]

    
