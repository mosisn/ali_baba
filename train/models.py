from django.db import models
from django.db.models import CharField


class TrainStation(models.Model):
    name = models.CharField(max_length=255)
    No = models.CharField(max_length=10)
    city = models.CharField(max_length=255, choices=[('TEH', 'Tehran'),
                                                     ('ISF', 'Isfahan'),
                                                     ('MSH', 'Mashhad'),
                                                     ('KRJ', 'Karaj'),
                                                     ('DEZ', 'Dezful'),])
    address = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=12)
    open_time = models.TimeField()
    close_time = models.TimeField()
    #
    # def __str__(self) -> str:
    #     return f'{self.name} - {self.No}'

    # class Meta:
    #     verbose_name = 'Kelaasor Airports'


class Train(models.Model):
    origin = models.ForeignKey(TrainStation, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(TrainStation, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=10, verbose_name='code')
    capacity = models.IntegerField()
    price = models.FloatField(help_text='price in Rial')
    #
    # def __str__(self) -> str:
    #     return f'{self.name} - {self.number}'

    # class Meta:
    #     verbose_name = 'Kelaasor Flights'

