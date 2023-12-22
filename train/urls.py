from django.urls import path
from .views import train_list, train_station_list, train_filter
urlpatterns = [
    path('list', train_list, name='train_list'),
    path('list2', train_station_list, name='train_station_list'),
    path('list3', train_filter, name='train_filter')
]