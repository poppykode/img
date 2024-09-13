from django.urls import path
from . import views

app_name = 'stations'

urlpatterns = [
    path('first-level-stations',views.first_level_stations,name='first_level_stations'),
    path('create-first-level-station',views.create_first_level_station,name='create_first_level_station'),
    path('edit-first-level-station/<int:id>',views.edit_first_level_station,name='edit_first_level_station'),
    path('delete-first-level-station/<int:id>',views.delete_first_level_station,name='delete_first_level_station'),

    path('second-level-stations',views.second_level_stations,name='second_level_stations'),  
    path('create-second-level-station',views.create_second_level_station,name='create_second_level_station'),
    path('edit-second-level-station/<int:id>',views.edit_second_level_station,name='edit_second_level_station'),
    path('delete-second-level-station/<int:id>',views.delete_second_level_station,name='delete_second_level_station'),

    path('third-level-stations',views.third_level_stations,name='third_level_stations'),
    path('create-third-level-stations',views.create_third_level_station,name='create_third_level_station'),
    path('edit-third-level-station/<int:id>',views.edit_third_level_station,name='edit_third_level_station'),
    path('delete-third-level-station/<int:id>',views.delete_third_level_station,name='delete_third_level_station'),

    path('station-creator/',views.station_creator,name='station_creator'),
    path('stations-admin/',views.stations_admin,name='stations'),

    path('stations',views.first_level_station_view,name='first_level_station_view'),
    path('stations/2/<int:id>',views.second_level_station_view,name='second_level_station_view'),
    path('stations/3/<int:id>',views.third_level_station_view,name='third_level_station_view'),

    path('stations-menu/<int:id>/<str:title>',views.stations_menu_view,name='stations_menu_view'),
    path('station-practice/<int:id>/<str:type>',views.station_practice,name='station_practice'),

]