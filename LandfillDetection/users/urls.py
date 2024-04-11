from rest_framework import routers
from .views import UserRegister, MyTokenObtainPairView, VerifyTokenView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import AdministratorCreateUserView


urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', VerifyTokenView.as_view(), name='token_verify'),
    path('admin/create_user/', AdministratorCreateUserView.as_view(), name='admin-create-user'),

]