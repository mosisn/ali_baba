from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport


def flight_list(request):
    flight = Flight.objects.all()
    flights = []
    for item in flight:
        dictionary = {
            "name": item.name,
            "origin": item.origin.name,
            "destination": item.destination.name,
            "price": item.price
        }
        flights.append(dictionary)
    return HttpResponse(flights)


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
    return HttpResponse(airports)
