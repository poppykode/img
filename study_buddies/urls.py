from django.urls import path
from . import views


app_name = 'study_buddies'
urlpatterns = [
    path('all',views.view_all_study_buddies, name='view_all_study_buddies')

]
