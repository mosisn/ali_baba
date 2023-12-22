from django.urls import path
from .views import flight_list, airport_list, test_list
urlpatterns = [
    path('list', flight_list, name='flight_list'),
    path('list2', airport_list, name='airport_list'),
    path('test-list', test_list, name='test_list')
]
