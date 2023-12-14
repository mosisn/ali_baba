from django.urls import path
from .views import flight_list
urlpatterns = [
    path('list', flight_list, name='flight_list')
]
