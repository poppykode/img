from django.urls import path
from . import views


app_name = 'coaches'
urlpatterns = [
    path('all',views.view_all_coaches, name='view_all_coaches')
]
