"""Creation of custom user."""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from core.managers.custom_user_manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('M', 'Mediator'),
        ('H', 'Hospital'),
        ('N', 'Nurse'),
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    username = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    validate_account = models.BooleanField(default=False)
    email = models.EmailField(null=True, max_length=300, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)

    objects = CustomUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_type']


