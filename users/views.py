from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()
# for registration
class UserRegistrationView(CreateAPIView):
    """
    Endpoints for User registration and Login
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

# For login
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

