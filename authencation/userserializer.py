from rest_framework import serializers
from .models import User





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, min_length=6,
                                     write_only=True)
    
    class Meta:
         model = User
         fields = ('id', 'email', 'username', 'password')
        
    def create(self, validated_data):
         user = User.objects.create_user(**validated_data)
         return user
       

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, min_length=6,
                                     write_only=True)
    
    class Meta:
         model = User
         fields = ( 'email', 'password')
        
        
   
       