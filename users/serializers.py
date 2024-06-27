from rest_framework import serializers
from.models import CustomUser
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UsersSerializer(serializers.ModelSerializer):
    #This serializer validates email and password fields using Django's built-in validators.
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")

    def validate_password(self, value):
        #Validate password using Django's password validation.
        try:
            validate_password(value) #value (str): Password to be validated.
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value #str: Validated password.

    def create(self, validated_data): #Create a new CustomUser instance.
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance #Newly created user instance.


