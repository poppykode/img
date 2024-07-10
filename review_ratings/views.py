from django.shortcuts import render, get_object_or_404,redirect
from . import models
from accounts.models import  User
from offers.models import Offer
from django.contrib import messages

# Create your views here.
def create_review(request,user_id):
    url = request.META.get('HTTP_REFERER')
    user_ = request.user
    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            rating = request.POST.get('rating')
        else:
            rating = 0.0
        review = request.POST.get('review')
        user_rated = get_object_or_404(User,id=user_id)
        user_has_commented = models.ReviewRating.objects.filter(user_rating=user_,user_rated=user_rated).exists()
        if not user_has_commented:
            new_rating = models.ReviewRating.objects.create(
                user_rating = user_,
                review = review,
                rating = rating,
                user_rated = user_rated,
                ip=request.META.get('REMOTE_ADDR')
            )
            if new_rating.id:
                obj, _ = models.AvgRating.objects.get_or_create(user_avg_rating=user_rated,defaults={ 'user_avg_rating':user_rated,'avg_rating':user_rated.averageReview()})
                if obj:
                    obj.avg_rating=user_rated.averageReview()
                    obj.save()
            messages.success(request, 'Review successfully updated.')
        else:
            messages.warning(request, 'You can only submit one review.')
    return redirect(url)


def create_offer_review(request,product_id):
    url = request.META.get('HTTP_REFERER')
    user_ = request.user
    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            rating = request.POST.get('rating')
        else:
            rating = 0.0
        review = request.POST.get('review')
        offer = get_object_or_404(Offer,id=product_id)
        #user_has_commented = models.ReviewRating.objects.filter(user_rating=user_,user_rated=user_rated).exists() 
        new_rating = models.OfferReviewRating.objects.create(
            user = user_,
            review = review,
            rating = rating,
            offer = offer,
            ip=request.META.get('REMOTE_ADDR')
        ) 
        messages.success(request, 'Review successfully updated.')
    else:
        messages.warning(request, 'You can only submit one review.')
    return redirect(url)

