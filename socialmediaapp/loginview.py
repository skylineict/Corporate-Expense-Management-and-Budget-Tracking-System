from rest_framework.generics import GenericAPIView
from .googleSerializer import GoogleSerializers
from .facebookserializer import FacebookSerializer
from  rest_framework.response import Response
from rest_framework import status



class GoogleloginVeiw(GenericAPIView):
    serializer_class = GoogleSerializers
    def post(self, request):
        seriilizer = self.serializer_class(data=request.data)
        seriilizer.is_valid(raise_exception=True)
        data = ((seriilizer.validated_data)['access_token'])
        return Response(data, status=status.HTTP_200_OK)
    

class Facebookclassview(GenericAPIView):
    serializer_class = FacebookSerializer
    def post(self, request):
        seriilizer = self.serializer_class(data=request.data)
        seriilizer.is_valid(raise_exception=True)
        data = ((seriilizer.validated_data)['access_token'])
        return Response(data, status=status.HTTP_200_OK)


