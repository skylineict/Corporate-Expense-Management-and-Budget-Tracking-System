from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

def LoginUser(email, password):
    user = authenticate(email=email, password=password)
    refresh_token = RefreshToken.for_user(user)
    return{
          "email": user.email,
             "username": user.username,
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),}