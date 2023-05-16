from rest_framework import serializers
from core.models.shift import Shift

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'hospital', 'location', 'time', 'date', 'price_per_hour']