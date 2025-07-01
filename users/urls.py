from django.urls import path
from .views import CustomTokenObtainPairView, UserRegistrationView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns =[
    path('login-token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("registration/", view=UserRegistrationView.as_view(), name="user_registration"),
]