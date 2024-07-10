from django.urls import path
from . import views


app_name = 'meeting_calendar'

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:id>/', views.CalendarView.as_view(), name='calendar'),
    path('availability/', views.availability, name='availability'),
    path('create-availability/', views.create_availability, name='create_availability'),
    path('remove-availability/<int:id>/', views.remove_availability, name='remove_availability'),
    path('check-in-or-check-out/', views.check_in_or_check_out, name='check_in_or_check_out')
]

