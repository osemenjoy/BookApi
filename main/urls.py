from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the root page!")

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path("api/", include("users.urls")),
    path("api/all_books/", include("books.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name="redoc",), 
]


