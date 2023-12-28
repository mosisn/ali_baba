from .models import TrainStation
from rest_framework.serializers import ModelSerializer


class TrainStationSerializer(ModelSerializer):
    class Meta:
        model = TrainStation
        fields = '__all__'
