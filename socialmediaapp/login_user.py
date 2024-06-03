from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

def LoginUser(email, password):
    print(email, password, "my passowrd and email")
    user = authenticate(email=email, password=password)
    print(user, 'here is my login')
    refresh_token = RefreshToken.for_user(user)
    return{
          "email": user.email,
             "username": user.username,
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),}