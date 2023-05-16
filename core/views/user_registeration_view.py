from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.custom_user_serializer import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from core.acl.custom_user_backend import CustomUserBackend
from core.acl.custom_user_check import IsCustomUser, IsHospitalUser
from core.models.custom_user import CustomUser

class UserRegistrationAPIView(APIView):
    # authentication_classes = [CustomUserBackend]
    permission_classes = [IsAuthenticated]

    def validate_permission(self, request, obj):
        if not obj.has_permission(request, self):
            return False
        return True

    def post(self, request):
        
        if not self.validate_permission(request, IsCustomUser()):
            return Response({'error': 'You are not authorized to create account.'}, status=status.HTTP_403_FORBIDDEN)

        data = request.data

        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, user_type):
        """View the users based upon the type."""
        try:
            if user_type == 'M':
                if not self.check_object_permissions(request, IsCustomUser()):
                    return Response({'error': 'You are not authorized to view mediator account.'}, status=status.HTTP_403_FORBIDDEN)
                mediators = CustomUser.objects.filter(user_type=user_type)
                result = CustomUserSerializer(mediators, many=True)
                return Response(result.data, status=status.HTTP_200_OK)
            elif user_type == 'H':
                # if not self.check_object_permissions(request, IsHospitalUser()) and not self.check_object_permissions(request, IsCustomUser()):
                #     return Response({'error': 'You are not authorized to view hospital account.'}, status=status.HTTP_403_FORBIDDEN)
                hospitals = CustomUser.objects.filter(user_type=user_type)
                result = CustomUserSerializer(hospitals, many=True)
                return Response(result.data,  status=status.HTTP_200_OK)
            else:
                nurses = CustomUser.objects.filter(user_type=user_type)
                result = CustomUserSerializer(nurses, many=True)
                return Response(result.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
