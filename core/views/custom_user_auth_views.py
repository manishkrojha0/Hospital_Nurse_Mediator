from typing import Any
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.serializers.auth_token_serializers import CustomTokenObtainPairSerializer
from core.serializers.custom_user_serializer import CustomUserSerializer
from core.managers.create_custom_user_token import CreateCustomUserToken

class CustomTokenObtainPairView(TokenObtainPairView):
    
    def __init__(self, **kwargs: Any) -> None:
        self.custom_token_mgr = CreateCustomUserToken()
        super().__init__(**kwargs)
    

    def post(self, request, *args, **kwargs):
        
        response_data = self.custom_token_mgr.generate_custom_user_token(request.data)

        if response_data:
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "No active account found with the given credentials"}, status=status.HTTP_400_BAD_REQUEST)

