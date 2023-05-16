from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from core.models.custom_user import CustomUser
from core.models.shift_application import ShiftApplication
from core.models.shift import Shift

class ShiftApplicationTest(APITestCase):

    def setUp(self):
        # Create a user and obtain a valid token
        self.hospital = CustomUser.objects.create_user(
            username='hospital', email='hospital@test.com', password='hospital', user_type='H'
        )
        self.nurse = CustomUser.objects.create_user(
            username='nurse', email='nurse@test.com', password='nurse', user_type='N'
        )
        self.shift = self.add_shift()
        self.token = self.get_token()
        self.client = APIClient()
        self.client.force_authenticate(user=self.nurse)

    def get_token(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(url, data)
        return response.data.get('access_token')
    
    def add_shift(self):
        shift = Shift.objects.create(hospital=self.hospital, location='Bengaluru', time="08:30", date="2023-06-17", price_per_hour = 400.00)
        return shift

    def add_shift_application(self):
        shift_application = ShiftApplication.objects.create(shift=self.shift, nurse=self.nurse)
        return shift_application
    
    def test_apply_shift_application(self):
        url = reverse('apply-shift', args=[self.shift.id])
        data = {
                "hospital": self.hospital.id,
                "location": "Bangalore rural",
                "time": "08:30",
                "date": "2023-05-17",
                "price_per_hour": 500.00
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_view_all_shift_applications(self):
        """View all the shifts."""
        self.add_shift_application()  # adding the shift application to test
        url = reverse('view-shift-applications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_select_nurse(self):
        """select nurse."""
        self.client.force_authenticate(user=self.hospital) # only hospital can select nurse.
        shif_application = self.add_shift_application()
        url = reverse('select-nurse', args=[self.shift.id, shif_application.id])
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
