from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from rest_framework.response import Response
from  .models import User
from django.conf import settings
from .email_otp_gen  import  send_otp
from .emailserializer import EmailSerializerVeiw
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class EmailVerificationView(GenericAPIView):
    serializer_class = EmailSerializerVeiw
    request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['otp_code'],
            properties={
                'otp_code': openapi.Schema(type=openapi.TYPE_STRING, description='email verification otp'),}
        )
   
   
    @swagger_auto_schema(request_body=request_body )
    def post(self, request):
        """

        Emial Verification Endpoint

        This view allows to enter the otp send to they email
        after account has been created. this endpoint will change the email to is_verified to true
        you are requried to passewors <b>otp_code<b/> as a paramater
      
        """
       
       
        
        verification_code = request.data.get('otp_code')  
        print(verification_code)
        try: 
            user = User.objects.get(otp_code=verification_code) 
            if not verification_code:
                return Response({'error': 'Verification code is not provided'}, status=status.HTTP_400_BAD_REQUEST)
            print(user)
            if user.otp_code != verification_code:
                return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
            if user.is_otp_expired():
                send_otp(user.email)  # Generate and send new OTP
                return Response({'message': 'Verification code expired. New code sent to your email'}, status=status.HTTP_200_OK)
               
            if user.is_verifiedemail:
                 return Response({'message': 'email already verified'}, status=status.HTTP_208_ALREADY_REPORTED)

            
            
            user.is_verifiedemail = True
            user.save()
            return Response({'message': 'email verified proceed to login'}, status=status.HTTP_200_OK)


        except User.DoesNotExist:
            return Response({'message':'account with provided otp not found'}, status=status.HTTP_404_NOT_FOUND)
       