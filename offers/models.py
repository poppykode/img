from django.db import models
from django.conf import settings
from django.db.models import Avg, Count
from tinymce.models import HTMLField



User = settings.AUTH_USER_MODEL
# Create your models here.

class OfferReviewRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_review')
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE,related_name='offer_review')
    review = HTMLField()
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ["timestamp",]

class Offer(models.Model):
    PENDING ='pending'
    STATUS = (('accepted','Accepted'),('rejected','Rejected'),(PENDING,'Pending'))
    user=models.ForeignKey(User,related_name='user_offers', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='offers')
    file = models.FileField(upload_to='files', null=True,blank=True)
    summary = HTMLField()
    description = HTMLField()
    price = models.FloatField(default=0.00)
    status = models.CharField(max_length=10,choices=STATUS,default=PENDING)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]


    def averageReview(self):
        reviews = OfferReviewRating.objects.filter(offer=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = OfferReviewRating.objects.filter(offer=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count




