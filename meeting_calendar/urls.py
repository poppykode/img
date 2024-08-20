from django.urls import path
from . import views


app_name = 'meeting_calendar'

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:id>/', views.CalendarView.as_view(), name='calendar'),
    path('availability/', views.availability, name='availability'),
    path('availability/<uuid:user_id>/', views.availability, name='availability'),
    path('create-availability/', views.create_availability, name='create_availability'),
    path('remove-availability/<int:id>/', views.remove_availability, name='remove_availability'),
    path('remove-availability/<int:id>/<str:action>/', views.remove_availability, name='remove_availability'),
    path('book-a-meeting/<uuid:user_id>/', views.book_a_meeting, name='book_a_meeting'),
    path('meeting_detail/<int:meeting_id>/', views.meeting_detail, name='meeting_detail'),
    path('check-in-or-check-out/<int:meeting_id>/<str:check_type>/', views.check_in_or_check_out, name='check_in_or_check_out'),
    path('update-meeting-status/<int:meeting_id>/<str:status_type>/', views.update_meeting_status, name='update_meeting_status'),
    path('create-a-quick-meeting/',views.create_a_quick_meeting,name="create_a_quick_meeting"),
    path('accept-a-quick-meeting/<int:id>/',views.accept_a_quick_meeting,name="accept_a_quick_meeting"),
    path('meetings/',views.meetings,name="meetings"),

    # API
    path('get-availability/<uuid:requested_user_id>/<str:booking_date>/', views.get_availability,name='get_availability')
]

