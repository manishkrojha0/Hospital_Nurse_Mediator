from core.models.custom_user import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

class CreateCustomUserToken(object):
    """Crate token for custom user model."""

    def __init__(self) -> None:
        pass
    
    def load_by_username(self, username):
        try:
            custom_user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            custom_user = None
        
        return custom_user

    def generate_custom_user_token(self, data):
        """generate token."""
        custom_user = self.load_by_username(data.get('username'))
        if custom_user:
            refresh = RefreshToken.for_user(custom_user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            result = {
                "user_id": custom_user.id,
                "username": custom_user.username,
                "email": custom_user.email,
                "access_token": access_token,
                "refresh_token": refresh_token
            }

            return result
        else:
            
            return None
    