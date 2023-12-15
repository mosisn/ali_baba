from django.contrib.admin import ModelAdmin, register
from .models import Train, TrainStation


@register(Train)
class TrainAdmin(ModelAdmin):
    autocomplete_fields = ['origin', 'destination']


@register(TrainStation)
class TrainStationAdmin(ModelAdmin):
    list_display = ['name', 'No', 'phone_number']
    search_fields = ['name', 'city']
    list_filter = ['name', 'city']

