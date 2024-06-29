from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import re_path as url
from .views import *


router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('search_books', BookSearchViewSet, basename='search_books')
urlpatterns = [
    url(r'', include(router.urls)),
]
