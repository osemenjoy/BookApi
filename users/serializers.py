from rest_framework import serializers
from.models import CustomUser
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")


class TokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=500, required=True)

    def create(self, validated_data):
        refresh = validated_data.get('refresh_token')
        try:
            # generate a new access token using the refresh token
            refresh_token = RefreshToken(refresh)
            access_token = str(refresh_token.access_token)
            return access_token
        except Exception as e:
            raise Exception(str(e))

class RegistrationSerializer(serializers.Serializer):
    #This serializer validates email and password fields using Django's built-in validators.
    username = serializers.CharField(max_length=500, required=True)
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def validate_password(self, value):
        #Validate password using Django's password validation.
        try:
            validate_password(value) #value (str): Password to be validated.
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value #str: Validated password.
