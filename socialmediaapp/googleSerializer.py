from rest_framework import serializers
from .googles import Google
from decouple import config
from rest_framework.exceptions import AuthenticationFailed
from .register import register_users

class GoogleSerializers(serializers.Serializer):
    access_token = serializers.CharField(min_length=20)
    def validate_access_token(self, access_token):
        google_user_data = Google.validate(access_token)
        
        print('here is the aud: ', google_user_data['aud'])
        print(google_user_data)

        

        try:
            google_user_data['sub']

        except:
            raise serializers.ValidationError('The token is invalid or expired. Please login again.')
        if google_user_data['aud'] != config('GOOGLE_CLIENT_ID'):
             raise AuthenticationFailed('couldnt not verifiy user')
        email = google_user_data['email']
        first_name = google_user_data['given_name']
        last_name = google_user_data['family_name']
        provider = 'google'
        return register_users(provider, email, first_name, last_name)

    