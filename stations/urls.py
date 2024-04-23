from django.urls import path
from . import views

app_name = 'stations'

urlpatterns = [
    path('all',views.stations,name='stations'),
    path('create-station',views.create_station,name='create_station'),
    path('edit-station/<int:id>',views.edit_station,name='edit_station'),
    path('delete-station/<int:id>',views.delete_station,name='delete_station'),

    path('station-categories',views.station_categories,name='station_categories'),  
    path('create-category-station',views.create_category_station,name='create_category_station'),
    path('edit-category-station/<int:id>',views.edit_category_station,name='edit_category_station'),
    path('delete-category-station/<int:id>',views.delete_category_station,name='delete_category_station'),

    path('station-sub-categories',views.station_sub_categories,name='station_sub_categories'),
    path('create-category-sub-station',views.create_category_sub_station,name='create_category_sub_station'),
    path('edit-sub-category-station/<int:id>',views.edit_sub_category_station,name='edit_sub_category_station'),
    path('delete-sub-category-station/<int:id>',views.delete_sub_category_station,name='delete_sub_category_station'),

]