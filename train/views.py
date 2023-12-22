from django.http.response import HttpResponse, JsonResponse
from .models import Train, TrainStation
from django.shortcuts import render
from datetime import datetime


def train_list(request):
    train = Train.objects.all()
    trains = []
    for item in train:
        dictionary = {
            "name": item.name,
            "origin": item.origin.name,
            "destination": item.destination.name,
            "price": item.price
        }
        trains.append(dictionary)
    return JsonResponse(trains, safe=False)


def train_station_list(request):
    train_station = TrainStation.objects.all()
    train_stations = []
    for item in train_station:
        dictionary = {
            "name": item.name,
            "number": item.No,
            "city": item.city,
        }
        train_stations.append(dictionary)
    return JsonResponse(train_stations, safe=False)

def train_filter(request):
    today = datetime.today().date()
    trains = Train.objects.filter(origin__city='TEH')
    t_list = {
        'trains' : trains
    }
    return render(request, 'trains/list.html', context=t_list)

