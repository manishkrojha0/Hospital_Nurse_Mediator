from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from core.models.custom_user import CustomUser

class JwtAuthenticationTests(APITestCase):

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

    def test_token_verify_url(self):
        # print(self.get_token())
        url = reverse('token_verify')
        data = {
            "token": self.token
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
