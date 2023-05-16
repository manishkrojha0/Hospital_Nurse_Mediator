"""Shift application model."""
from django.db import models
from core.models.custom_user import CustomUser
from core.models.shift import Shift

class ShiftApplication(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='applications')
    nurse = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'N'}, related_name='applications')
    selected = models.BooleanField(default=False)
