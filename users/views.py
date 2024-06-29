from django.shortcuts import render
from .models import CustomUser
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, logout 
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from django.db import transaction



class RegisterView(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        with transaction.atomic():
            try:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                email = serializer.validated_data.get(email)
                password = serializer.validated_data.get(password)
                username = serializer.validated_data.get(username)
                if CustomUser.objects.filter(email=email).exists():
                    raise Exception ("A user with this email address alredy exists")
                user = CustomUser.objects.create_user(email=email, password=password, username=username)
                return Response(
                    {
                    "message": "User created successfully", 
                    "status": "Success",
                    "data": UsersSerializer(user).data,
                }, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response(
                {
                    "status": "failed",
                    "message": f"Registration Unuccessful: {e}",
                    "data": [],

                },
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']

            user = CustomUser.objects.filter(email=email).first()

            if user is None:
                raise AuthenticationFailed("User not found")

            if not user.check_password(password):
                raise AuthenticationFailed("password is Incorrect")

            refresh = RefreshToken.for_user(user)
            login(request, user)
            userdata = UsersSerializer(user).data
            return Response(
                {
                    "status": "success",
                    "message": "login Successful",
                    "data": userdata, 
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),

                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
            {
                "status": "failed",
                "message": f"login Unuccessful: {e}",
                "data": [],
                "refresh": None,
                "access": None,

            },
            status=status.HTTP_400_BAD_REQUEST
        )

class TokenRefreshView(GenericAPIView):
    """A view to refresh the access token, by using the refresh token"""
    serializer_class = TokenRefreshSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            self.serializer = self.get_serializer_class()
            self.serializer = self.serializer(data=request.data)
            self.serializer.is_valid(raise_exception=True)
            access_token = self.serializer.save()
            return Response(
            {
                "status": "success",
                "message": "Token refresh Successful",
                "data": access_token, 

            },
            status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
            {
                "status": "failed",
                "message": "Token refresh Unsuccessful",
                "data": [], 

            },
            status=status.HTTP_200_OK
            )            
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer
