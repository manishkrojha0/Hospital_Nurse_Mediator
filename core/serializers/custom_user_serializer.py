from rest_framework import serializers
from core.models.custom_user import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'user_type', 'address', 'email']
