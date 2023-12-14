from django.contrib.admin import ModelAdmin, register
from .models import Flight, Airport


@register(Flight)
class FlightAdmin(ModelAdmin):
    autocomplete_fields = ['origin']


@register(Airport)
class AirportAdmin(ModelAdmin):
    list_display = ['name', 'No', 'phone_number']
    search_fields = ['name', 'city']
    list_filter = ['name', 'city']
