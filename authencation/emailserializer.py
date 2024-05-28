from .models import User
from rest_framework import serializers



class EmailSerializerVeiw(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['otp_code']


        

        
