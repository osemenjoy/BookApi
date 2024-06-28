from django.urls import re_path as url 
from .views import *
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import re_path as url


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
urlpatterns = [
    url(r'', include(router.urls)),
]
urlpatterns = [
    url(r'', include(router.urls)),
    url('register/', RegisterView.as_view(), name="register"),
    url('login/', LoginView.as_view(), name="login"),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),

]
