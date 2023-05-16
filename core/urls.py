"""Urls for core app."""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from core.views.toke_verification_view import TokenVerificationAPIView
from .views.custom_user_auth_views import CustomTokenObtainPairView
from core.views.user_registeration_view import UserRegistrationAPIView
from core.views.shift_view import ShiftAPIView
from core.views.shift_application_view import ShiftApplicationAPIView

urlpatterns = [
    path('api/token/verify/', TokenVerificationAPIView.as_view(), name='token_verify'),
    path('api/authenticate/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/user/<str:user_type>/', UserRegistrationAPIView.as_view(), name='view-users'),
    path('api/shifts/', ShiftAPIView.as_view(), name='shifts'),
    path('api/shifts/applications/', ShiftApplicationAPIView.as_view(), name='view-shift-applications'),
    path('api/shifts/<int:shift_id>/apply/', ShiftApplicationAPIView.as_view(), name='apply-shift'),
    path('api/shifts/<int:shift_id>/applications/<int:application_id>/select/', ShiftApplicationAPIView.as_view(), name='select-nurse'),

]