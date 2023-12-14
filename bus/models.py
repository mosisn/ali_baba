from django.db import models


class Terminal(models.Model):
    name = models.CharField(max_length=255)
    No = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=12)
    open_time = models.TimeField()
    close_time = models.TimeField()


class Buses(models.Model):
    origin = models.ForeignKey(Terminal, on_delete=models.CASCADE, default=None, related_name='origin')
    destination = models.ForeignKey(Terminal, on_delete=models.CASCADE, default=None, related_name='destination')
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price = models.FloatField()
