from django.urls import path
from . import views


app_name = 'meeting_calendar'

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:id>/', views.CalendarView.as_view(), name='calendar'),
    path('availability/', views.availability, name='availability'),
    path('create-availability/', views.create_availability, name='create_availability')
]

