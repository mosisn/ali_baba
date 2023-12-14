from django.urls import path
from .views import flight_list, airport_list
urlpatterns = [
    path('list', flight_list, name='flight_list'),
    path('list2', airport_list, name='flight_list')
]
