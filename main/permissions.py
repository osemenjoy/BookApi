from rest_framework import permissions
from users.models import CustomUser


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        app_user = CustomUser.objects.get(username=request.user.username)
        return (request.user.is_authenticated and app_user.user_type == "admin") or request.method in permissions.SAFE_METHODS