from .userserializer import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework import response, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import User
import jwt
from django.conf import settings


class TokenVerfication(GenericAPIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            Response({'message':"Token not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
             payload = jwt.decode(token,settings.SECRET_KEY, algorithm='HS256')
             print(payload)
        except  jwt.ExpiredSignatureError:
             Response({'message':"expired Token"}, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.filter(id=payload['id']).first()
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)



       
    
    