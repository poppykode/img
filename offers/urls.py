from django.urls import path
from . import views


app_name = 'offers'
urlpatterns = [
    path('offer-details/<int:offer_id>',views.offer_details, name='offer_details'),  
    path('create-offer',views.create_offer, name='create_offer'),
    path('offers',views.offers, name='offers'),
    # to be delete
    path('create-offer-json',views.create_offer_json, name='create_offer_json'),
    path('accept-or-reject-offer/<int:offer_id>/<str:status>',views.accept_or_reject_offer, name='accept_or_reject_offer'),
]
