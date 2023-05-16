from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from core.models.custom_user import CustomUser

class ProfileTest(APITestCase):

    def setUp(self):
        # Create a user and obtain a valid token
        self.user = CustomUser.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass', user_type='M'
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

    
    def test_user_register_url(self):
        url = reverse('user-register')
        data = {
            'username': 'newuser',
            'password': 'newpass',
            'user_type': 'H',
            'name': "newH"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_view_users(self):
        """Test the users type available."""
        url = reverse('view-users', args=['N'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
