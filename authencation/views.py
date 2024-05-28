from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from rest_framework.response import Response
from .userserializer import UserSerializer,LoginSerializer
from django.contrib.auth import authenticate
from  .models import User
import os
from django.conf import settings
from datetime import timedelta

from rest_framework_simplejwt.tokens import RefreshToken
from .email_otp_gen  import  send_otp,generate_otp
from rest_framework_simplejwt.tokens import RefreshToken
import pyotp
from rest_framework.response  import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renders import UserRenders
from decouple import config

# Create your views here.
class Registeration(GenericAPIView):
    serializer_class = UserSerializer
    renderer_classes = (UserRenders,)
    request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email','password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email address'),
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password')
                
                }
        )
   
   

   
    @swagger_auto_schema(request_body=request_body )
    def post(self,request):
        """User registration

        This view allows to enter register account as a  new use
        you are requred to pass the follwing paramater 
        <b>email, username, password<b/>
        
      
        """
        
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            user_email = serialized_data.data.get('email')
            send_otp(user_email)
            # print(user_email)
            # print(send_otp)
            return Response({'message': "Account created. OTP has been sent to your email.", 'data': serialized_data.data}, status=status.HTTP_201_CREATED)

        return response.Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    



 # Import response and rename it






class Login(GenericAPIView):
    serialized_data =LoginSerializer
    request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email','password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password')
                           }
        )
   
    @swagger_auto_schema(request_body=request_body )
    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({"error": "invalid email or pasword"}, status=status.HTTP_400_BAD_REQUEST)
        if not User.objects.filter(email=email).exists():
             return Response({'message': "Email not found "}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_verifiedemail:
               send_otp(user.email)
               return Response({'message': "Email is not verified, kindly, otp has been sent to your email to verify and continue logging "}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.check_password(password):
            return Response({'message': "Incorrect password "}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        refresh.set_exp(lifetime=timedelta(days=30))
        # Extend refresh token expiration to 30 days
      
        # payload  ={
        #     'id': user.id,
        #     'exp': datetime.utcnow() + timedelta(minutes=180)

        # }i
       
      
        
      
        mykeys = config('GOOGLE_CLIENT_ID')
        import  pdb
        pdb.set_trace()
        # token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='Token', value=str(refresh.access_token), httponly=True)
        response.data = {
             "email": user.email,
             "username": user.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
           
            
        }

         # Extend access token expiration to 1 hour
        access_token = refresh.access_token
        access_token.set_exp(lifetime=timedelta(hours=1))
        response.data['access'] = str(access_token)
        return response



