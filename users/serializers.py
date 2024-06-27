from rest_framework import serializers
from .models import CustomUser
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UsersSerialiazer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "email")


    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise Serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        users = CustomUser.objects.create(
            username= validated_data['username'],
            email = validated_data['email']
        )
        user.set_password = validated_data['password']
        user.save()
        return user