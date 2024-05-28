from .passwordserializer import ChangePasswordSerializer
from rest_framework.views import APIView
from .models import User,UserVerification
from .email_otp_gen import send_password_reset_email
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



    

class ChangepasswordView(APIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['password', 'confirm_password'],
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='New password'),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING, description='Confirm new password'),}
        )
   
   
    @swagger_auto_schema(request_body=request_body )
    def post(self, request):
        """
        Change password view

        This view allows authenticated users to change their password.

        Parameters:
        password (string): New password
        confirm_password (string): Confirm new password

        Returns:
        message (string): Password updated successfully
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            confirm_password = serializer.validated_data['confirm_password']
            user=request.user
            user.set_password(password)
            user.save()
            return Response({'message': 'Password updated successfully'})
        return Response(serializer.errors, status=400)