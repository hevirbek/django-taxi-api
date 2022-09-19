from rest_framework import serializers
from .models import Taxi, TaxiRequest


class TaxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = ('__all__')


class TaxiRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxiRequest
        fields = ('__all__')
