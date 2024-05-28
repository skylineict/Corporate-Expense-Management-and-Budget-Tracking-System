from .passwordserializer import PasswordResetSerializer,SetPasswordserializer,LogoutSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.permissions import IsAuthenticated


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response({'message':'a link has been sent to your email to Reset your password'}, status=status.HTTP_200_OK)
    

class PasswordcomfirmReset(GenericAPIView):
    def get(self,request,uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)
            tokencheck = PasswordResetTokenGenerator().check_token(user,token)
            if not tokencheck:
                return Response({"error": 'token is invalid or has expired'}, status=status.HTTP_400_BAD_REQUEST)
            res = {
                 'user':user.email,
                 'uidb64': uidb64,
                 'token': token,
                  'sucess':"password token is verified"
             }
            return Response(res,status=status.HTTP_200_OK)
        except  DjangoUnicodeDecodeError:
            return Response({"error":"user link is not valide"}, status=status.HTTP_404_NOT_FOUND)


class SetPasswordView(GenericAPIView):
     serializer_class = SetPasswordserializer
     def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message':'new password set sucessfully'}, status=status.HTTP_200_OK)

class Logoutveiw(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



            
    