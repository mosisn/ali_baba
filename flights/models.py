from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=255)
    No = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=12)
    open_time = models.TimeField()
    close_time = models.TimeField()


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price = models.FloatField()
