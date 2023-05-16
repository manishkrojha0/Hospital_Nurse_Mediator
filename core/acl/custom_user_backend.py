"""We create a custom user backend to define how the authentication process should work for
   our custom user model (CustomUser in this case).
   The default authentication backend in Django (django.contrib.auth.backends.ModelBackend)
   is designed to work with the built-in User model provided by Django. However, when we
   introduce a custom user model, we need to create a custom authentication backend to
   handle the authentication process specifically for our custom user model.
"""

from django.contrib.auth.backends import BaseBackend
from core.models.custom_user import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)

            if user.check_password(password):
                return user
            else:
                return None

        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
