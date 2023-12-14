from django.http.response import HttpResponse, JsonResponse
from .models import Flight


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
