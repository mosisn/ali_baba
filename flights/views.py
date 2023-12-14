from django.http.response import HttpResponse, JsonResponse
from .models import Flight


def flight_list(request):
    flight_info = {
        'name': 'airbus',
        'number': '513',
        'capacity': 255,
        'price': 650000.0
        }
    return JsonResponse(flight_info)
