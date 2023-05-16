from django.db import models
from core.models.custom_user import CustomUser

class Shift(models.Model):
    hospital = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return "time: " + str(self.time) + " date: " + str(self.date)