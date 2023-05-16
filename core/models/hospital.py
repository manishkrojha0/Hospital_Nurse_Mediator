from django.db import models
from core.models.custom_user import CustomUser

class Hospital(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='hospital')

    def __str__(self) -> str:
        return self.user.username
