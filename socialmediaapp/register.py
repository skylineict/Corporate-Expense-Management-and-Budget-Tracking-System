from django.contrib.auth import get_user_model
from authencation.models import User
from .login_user import LoginUser
from decouple import config
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import random


def user_generate(name):
    User = get_user_model()
    username = name
    
    while User.objects.filter(username=username).exists():
        generate_number = random.randint(100, 999)
        username = f"{username}{generate_number}"
    return username


def register_users(provider, email, name, id):
    print(provider, email, name, id)
    user = User.objects.filter(email=email)
    if user.exists():
        if provider == user[0].auth_user_provider:
            login_user = authenticate(email=email, password=config('SOCIAL_PASSWORD'))
            refresh_token = RefreshToken.for_user(login_user)
            return{
          "email": login_user.email,
             "username": login_user.username,
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),}
        else:
            raise AuthenticationFailed('Please continue your login using ' + user[0].auth_user_provider)
    else:
        # Create a new user without first_name and last_name
        username = user_generate(name)
        new_user = {
            "email": email,
            'id':  id,
            'username': username ,
            'password': config('SOCIAL_PASSWORD')
        }
        user_model = get_user_model()
        register_user = user_model.objects.create_user(**new_user)
        # print('here is my registration',register_user,)

        # Additional fields specific to your User model can be set here
        register_user.auth_user_provider = provider
        register_user.is_verifiedemail = True
        register_user.save()
       

        login_user = authenticate(email=email, password=config('SOCIAL_PASSWORD'))
        refresh_token = RefreshToken.for_user(login_user)
        return{
          "email": login_user.email,
             "username": login_user.username,
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),}