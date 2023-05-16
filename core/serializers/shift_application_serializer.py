
from rest_framework import serializers
from core.models.shift_application import ShiftApplication
from core.serializers.shift_serializer import ShiftSerializer
from core.serializers.custom_user_serializer import CustomUserSerializer


class ShiftApplicationSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer(read_only=True)
    nurse = CustomUserSerializer(read_only=True)
    class Meta:
        model = ShiftApplication
        fields = ['id', 'shift', 'nurse', 'selected']