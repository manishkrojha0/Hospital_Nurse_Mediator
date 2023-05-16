"""This file is created for applying the validation on custom user."""

from rest_framework.permissions import BasePermission

class IsCustomUser(BasePermission):
    def has_permission(self, request, view):

        user = request.user

        return user.user_type == 'M'  # Only allow Mediators

class IsHospitalUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return user.user_type == 'H' # Only allow Hospital

