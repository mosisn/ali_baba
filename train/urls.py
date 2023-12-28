from django.urls import path
from .views import (train_list, train_station_list,
                    train_today_onward, train_page,
                    train_past, TrainStationList,
                    CreateTrainStation, TrainStationView,
                    TrainStationdelete, TrainStationRetrieve,
                    TrainStationUpdate)
urlpatterns = [
    path('list', train_list, name='train_list'),
    path('list2', train_station_list, name='train_station_list'),
    path('list3', train_today_onward, name='train_filter'),
    path('list4', train_past, name='train_station_list'),
    path('create-trainstation', CreateTrainStation.as_view(), name='CreateTrainStation'),
    path('trainstation-list', TrainStationList.as_view(), name='trainstationlist'), 
    path('trainstation', TrainStationView.as_view(), name='trainstationView'),
    path('trainstation-delete/<int:pk>', TrainStationdelete.as_view(), name='TrainStationdelete'),
    path('trainstation-retrieve/<int:pk>', TrainStationRetrieve.as_view(), name='TrainStationRetrieve'), 
    path('trainstation-update/<int:pk>', TrainStationUpdate.as_view(), name='TrainStationRetrieve'),
    path('<str:code>', train_page, name='train_page'),
]