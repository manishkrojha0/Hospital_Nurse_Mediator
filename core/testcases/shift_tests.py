from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from core.models.custom_user import CustomUser

class ShiftTest(APITestCase):

    def setUp(self):
        # Create a user and obtain a valid token
        self.user = CustomUser.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass', user_type='H'
        )
        self.token = self.get_token()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def get_token(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(url, data)
        return response.data.get('access_token')

    
    def test_add_shift(self):
        url = reverse('shifts')
        data = {
                "hospital": self.user.id,
                "location": "Bangalore rural",
                "time": "08:30",
                "date": "2023-05-17",
                "price_per_hour": 500.00
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_view_all_shifts(self):
        """View all the shifts."""
        self.test_add_shift()  # adding the shift to test
        url = reverse('shifts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
