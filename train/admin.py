from django.contrib.admin import ModelAdmin, register
from .models import Train, TrainStation


@register(Train)
class FlightAdmin(ModelAdmin):
    autocomplete_fields = ['origin', 'destination']


@register(TrainStation)
class AirportAdmin(ModelAdmin):
    list_display = ['name', 'No', 'phone_number']
    search_fields = ['name', 'city']
    list_filter = ['name', 'city']

