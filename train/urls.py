from django.urls import path
from .views import train_list, train_station_list, train_today_onward, train_page,train_past
urlpatterns = [
    path('list', train_list, name='train_list'),
    path('list2', train_station_list, name='train_station_list'),
    path('list3', train_today_onward, name='train_filter'),
    path('list4', train_past, name='train_station_list'),
    path('<str:code>', train_page, name='train_page'),
]