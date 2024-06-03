from rest_framework import serializers
from .facebookutils import Facebook
from .register import register_users


class FacebookSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    email = serializers.EmailField(required=False)

    def validate_access_token(self, access_token):
        user_data = Facebook.validate(access_token)
        id = int(user_data['id'])
        name = user_data['name']
        email = self.initial_data.get('email', None)
        provider  = 'facebook' 
        if not email:
            raise serializers.ValidationError('Email is required for registration. Please provide your email.' )
        
        user = register_users(provider, email, name, id)
        print(user)
        return user