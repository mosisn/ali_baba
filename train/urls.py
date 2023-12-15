from django.urls import path
from .views import train_list, train_station_list
urlpatterns = [
    path('list', train_list, name='train_list'),
    path('list2', train_station_list, name='train_station_list')
]