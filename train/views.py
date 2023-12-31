from django.http.response import HttpResponse, JsonResponse
from .models import Train, TrainStation
from django.shortcuts import render
from datetime import datetime
from .serializers import TrainStationSerializer
from rest_framework import generics


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

def train_today_onward(request):
    today = datetime.today().date()
    trains = Train.objects.filter(time__date__gte = today).order_by('-price')
    t_list = {
        'trains' : trains
    }
    return render(request, 'trains/list.html', context=t_list)

def train_past(request):
    today = datetime.today().date()
    trains = Train.objects.filter(time__date__lt = today).order_by('capacity')
    t_list = {
        'trains' : trains
    }
    return render(request, 'trains/list_past.html', context=t_list)

def train_page (request, code):
    try:
        trains = Train.objects.get(number= code)
    except:
        trains = None
    t_list = {
        'trains' : trains
    }
    return render(request, 'trains/train_page.html', context=t_list)

class TrainStationList(generics.ListAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class CreateTrainStation(generics.CreateAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class TrainStationView(generics.ListCreateAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class TrainStationdelete(generics.DestroyAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class TrainStationRetrieve(generics.RetrieveAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class TrainStationUpdate(generics.UpdateAPIView):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer

class TrainStationView2(generics.RetrieveUpdateDestroyAPIView):
    #does the work of  all above three classes
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer