from django.shortcuts import render
from .models import CustomUser
from .serializers import UsersSerialiazer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerialiazer

