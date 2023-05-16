from django.db import models
from core.models.custom_user import CustomUser

class Nurse(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='nurse')

    def __str__(self) -> str:
        return self.user.username
