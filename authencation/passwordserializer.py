from rest_framework import serializers
from .models import User, UserVerification
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .email_otp_gen import sentpasswordemail
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=250)
    class Meta:
        fields = ['email']




    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            request = self.context.get('request')
            current_site = get_current_site(request).domain
            relativelink = reverse("reset-password-comfirm", kwargs={"uidb64":uidb64, "token":token})
            absurl = f"http://{current_site}{relativelink}"
            email_body = f"Dear {user.username} use the link below to Reset your password \n {absurl}"
            data = {
                "email_body": email_body,
                 "email_subject": "Password Reset",
                 "email_to": user.email
            }
            sentpasswordemail(data)
        else:
            raise AuthenticationFailed('email address provided not found')
        return super().validate(attrs)

  
        
class SetPasswordserializer(serializers.Serializer):
    password = serializers.CharField(max_length=250,write_only=True)
    comfirm_password = serializers.CharField(max_length=250, write_only=True)
    token =  serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)
  
    class Meta:
        fields =  ['password','comfirm_password','token','uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            comfirm_password = attrs.get('comfirm_password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            if password != comfirm_password:
                raise serializers.ValidationError("password not match")
            if len(password) < 8:
                raise serializers.ValidationError("password too short")
      
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            tokencheck = PasswordResetTokenGenerator().check_token(user,token)
            if not tokencheck:
                  raise AuthenticationFailed('token is invalid or has expired')
            user.set_password(password)
            user.save()
            return user
        except DjangoUnicodeDecodeError:
            raise AuthenticationFailed('user link is not valide')
            
                

       



        return super().validate(attrs)
           



class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs.get('refresh')
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({'refresh': 'Token is expired or invalid'})