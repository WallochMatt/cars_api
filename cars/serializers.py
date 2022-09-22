from rest_framework import serializers
from .models import Car # '.' shows files in the same folder

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price', 'color', 'dealership_id']