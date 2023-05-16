from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.shift_serializer import ShiftSerializer
from rest_framework.permissions import IsAuthenticated
from core.acl.custom_user_check import IsHospitalUser
from core.models.shift import Shift

class ShiftAPIView(APIView):

    permission_classes = [IsAuthenticated]
      
    def post(self, request):
        """add shifts."""
        
        if not IsHospitalUser().has_permission(request, self):
            return Response({'error': 'You are not authorized to add this shift.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ShiftSerializer(data=request.data)

        if serializer.is_valid():
            shift = serializer.save(hospital=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        """View all shifts."""
        shifts = Shift.objects.all()
        serializer = ShiftSerializer(shifts, many=True).data

        if serializer:
            return Response(serializer, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

