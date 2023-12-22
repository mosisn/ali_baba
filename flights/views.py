from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport
from django.shortcuts import render


def flight_list(request):
    flight = Flight.objects.all()
    flights = {
        'flights': flight
    }

    # return HttpResponse(flights)
    return render(request, 'flights/list.html', context=flights)


def airport_list(request):
    airport = Airport.objects.all()
    airports = []
    for item in airport:
        dictionary = {
            "name": item.name,
            "number": item.No,
            "city": item.city,
        }
        airports.append(dictionary)
    # return HttpResponse(airports)
    return render(request, 'flights/list2.html')

def test_list(request):
    flight = Flight.objects.filter()
    flights = {
        'flights': flight
    }

    # return HttpResponse(flights)
    return render(request, 'flights/list.html', context=flights)