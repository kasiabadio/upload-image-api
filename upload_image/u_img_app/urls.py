"""images URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .models import User, Image
from .serializers import UserSerializer, ImageSerializer
from rest_framework import generics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', generics.ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer)),
    path('images/', generics.ListCreateAPIView.as_view(queryset=Image.objects.all(), serializer_class=ImageSerializer)),
    path('images/<int:pk>/', views.ImageDetail.as_view()),
    path('login/', include('rest_framework.urls')),
]
