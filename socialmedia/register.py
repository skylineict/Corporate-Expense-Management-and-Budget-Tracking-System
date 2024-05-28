from django.contrib.auth import get_user_model
from authencation.models import User
from .login_user import LoginUser
from decouple import config
from rest_framework.exceptions import AuthenticationFailed

# Users = get_user_model

def register_users(provider, email, first_name, last_name):
    user = User.objects.filter(email=email)
    if user.exists():
        if provider == user[0].auth_user_provider:
            password = config('SOCIAL_PASSWORD')
            LoginUser(email,password)
        else:
            raise AuthenticationFailed('Please continue your login using' + user[0].auth_user_provider )
    else:
        new_user = {
            "email": email,
            "fist_name": first_name,
            "last_name": last_name
        }
        register_user = User.objects.create(**new_user)
        register_user.auth_user_provider = provider
        register_user.is_verifiedemail = True
        register_user.save()
        password = config('SOCIAL_PASSWORD')
        LoginUser(register_user.email,password)

        

