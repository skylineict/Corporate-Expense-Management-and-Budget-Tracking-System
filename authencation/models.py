from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from helperclass.models import Modeltracking
from django.contrib.auth.hashers import make_password
import jwt
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings
import pyotp
from shortuuid.django_fields import ShortUUIDField
# Create your models here.


class UserManager(BaseUserManager):
    

    def create_user(self,email,username=None,password=None,**extra_fields):
         
         if not email:
            raise ValueError('The given email must be set')
         email = self.normalize_email(email)
         user = self.model(email=email, **extra_fields)
         if username:
            user.username = username
         user.set_password(password)
         user.save(using=self._db)
         return user
        

    def _create_user(self,email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email,username,password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        username = email.split('@')[0]  # Use the part before '@' in the email
        return self.create_user(email, username=username, password=password, **extra_fields)
Auth_provider = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}
class User(Modeltracking,PermissionsMixin,AbstractBaseUser):
    id = ShortUUIDField(unique=True,primary_key=True, max_length=200,alphabet="abcdefghijklmnopqrstuvwxyz0123456789",prefix="usr-",editable=False,)
    username = models.CharField(max_length=150,unique=True,)
    email = models.EmailField( blank=False, unique=True)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    is_verifiedemail =  models.BooleanField(default=False,)
    otp_code = models.CharField(max_length=10)
    otp_sent_time = models.DateTimeField(null=True, blank=True)
    auth_user_provider =  models.CharField(default=Auth_provider.get('email'), max_length=300)
    full_name =  models.CharField(max_length=150,default='olisa')





    objects = UserManager()
    def is_otp_expired(self): 
        if not self.otp_sent_time:  # If OTP has not been sent yet
            return True
        
        validity_period = timedelta(minutes=4)  # Assuming OTP is valid for 30 minutes
        current_time = timezone.now()
        time_difference = current_time - self.otp_sent_time
        return time_difference > validity_period
    
    

   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32(), interval=240)  # OTP expires in 30 minutes
    return totp.now()

class UserVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6, blank=True)

    def generate_verification_code(self):
        self.verification_code = generate_otp()
        self.save()

