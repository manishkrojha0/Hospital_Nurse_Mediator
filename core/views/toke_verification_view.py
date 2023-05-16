from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.permissions import AllowAny 

class TokenVerificationAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validated_token = self.verify_token(token)

            return Response({'detail': 'Token is valid'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    def verify_token(self, token):
        try:
            # Attempt to verify the token
            validated_token = AccessToken(token)
            # The token is valid, return the validated token
            return validated_token
        except TokenError as e:
            # The token is invalid or expired
            raise InvalidToken(str(e))
