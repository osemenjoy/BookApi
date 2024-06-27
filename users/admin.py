from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "password"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age', )}), ) #Adds it to the change form field in the admin interface
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
