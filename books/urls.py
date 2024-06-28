from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import re_path as url
from .views import *


router = DefaultRouter()
router.register('add_books', BookViewSet, basename='add_books')
router.register('book_list', BookViewSet, basename='book_list')
router.register('search_books', BookSearchViewSet, basename='search_books')
router.register('edit_book', BookViewSet, basename='edit_book')
urlpatterns = [
    url(r'^all_books/$', BookViewSet.as_view({'get': 'list'})),  # new URL pattern
    url(r'^book/(?P<pk>\d+)$', BookViewSet.as_view({'get': 'retrieve'})),  # new URL pattern
    url(r'', include(router.urls)),
]
