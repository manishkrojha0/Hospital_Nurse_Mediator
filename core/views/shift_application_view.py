from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.shift_application_serializer import ShiftApplicationSerializer
from core.models.shift import Shift
from core.models.shift_application import ShiftApplication
from rest_framework.permissions import IsAuthenticated
from core.acl.custom_user_check import IsHospitalUser
from core.models.custom_user import CustomUser


class ShiftApplicationAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """View shift applications."""
         # only hospital can see the shift applications
        try:
            shift_applications = ShiftApplication.objects.all()
            results = ShiftApplicationSerializer(shift_applications, many=True).data
            return Response(results, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_200_OK)

    
    def post(self, request, shift_id):
        """to select the shift or apply the shift."""
        shift = Shift.objects.get(id=shift_id)
        nurse = CustomUser.objects.get(id=request.user.id, user_type='N')
        data = {
            "shift": shift_id,
            "nurse": nurse.id
        }
        serializer = ShiftApplicationSerializer(data=data)


        if serializer.is_valid():
            application = serializer.save(shift=shift, nurse=request.user)    # this is being done by nurses
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, shift_id, application_id):
        """Assign shift to the requested nurse."""

        # Perform permission check for hospital user
        if not IsHospitalUser().has_permission(request, self):
            return Response({'error': 'You are not authorized to modify this shift.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            shift = Shift.objects.get(id=shift_id)
            application = ShiftApplication.objects.get(id=application_id, shift=shift)

            # Perform other validations
            if shift.hospital != request.user:
                return Response({'error': 'You are not authorized to modify this shift.'}, status=status.HTTP_403_FORBIDDEN)

            if application.selected:
                return Response({'error': 'This application is already selected for the shift.'}, status=status.HTTP_400_BAD_REQUEST)

            # Assign the shift to the nurse
            application.selected = True
            application.save()

            return Response(status=status.HTTP_200_OK)
        except Shift.DoesNotExist:
            return Response({'error': 'Shift not found.'}, status=status.HTTP_404_NOT_FOUND)
        except ShiftApplication.DoesNotExist:
            return Response({'error': 'Shift application not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("error", str(e))
            return Response({'error': 'An error occurred.'}, status=status.HTTP_400_BAD_REQUEST)

    