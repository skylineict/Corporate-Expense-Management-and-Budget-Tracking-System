from rest_framework import serializers
from .google import Google

class GoogleSerializers(serializers.Serializer):
    access_token = serializers.CharField(min_length=20)
    def validate_access_token(self, access_token):
        google_user_data = Google.validate(access_token)