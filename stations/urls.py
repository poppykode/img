from django.urls import path
from . import views

app_name = 'stations'

urlpatterns = [
    path('all',views.first_level_stations,name='first_level_stations'),
    path('create-station',views.create_first_level_station,name='create_first_level_station'),
    path('edit-station/<int:id>',views.edit_first_level_station,name='edit_first_level_station'),
    path('delete-station/<int:id>',views.delete_first_level_station,name='delete_first_level_station'),

    path('station-categories',views.second_level_stations,name='second_level_stations'),  
    path('create-category-station',views.create_second_level_station,name='create_second_level_station'),
    path('edit-category-station/<int:id>',views.edit_second_level_station,name='edit_second_level_station'),
    path('delete-category-station/<int:id>',views.delete_second_level_station,name='delete_second_level_station'),

    path('station-sub-categories',views.third_level_stations,name='third_level_stations'),
    path('create-category-sub-station',views.create_third_level_station,name='create_third_level_station'),
    path('edit-sub-category-station/<int:id>',views.edit_third_level_station,name='edit_third_level_station'),
    path('delete-sub-category-station/<int:id>',views.delete_third_level_station,name='delete_third_level_station'),

]