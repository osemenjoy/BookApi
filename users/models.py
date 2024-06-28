from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_options= (
            ('user', 'User'),
            ('admin', 'Admin'),
        )    
    age = models.PositiveIntegerField(null=True, blank=True)
    user_type = models.CharField('User Type', choices=user_type_options, max_length=255, default='user')
