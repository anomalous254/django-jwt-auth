from django.urls import path
from .views import CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView ,SignOutView


urlpatterns = [
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='obtain_token'),
    path('jwt/refresh/', CustomTokenRefreshView.as_view(), name='refresh_token'),
    path('jwt/verify/', CustomTokenVerifyView.as_view(), name='verify_token'),
    path('jwt/signout/', SignOutView.as_view(), name='sign_out'),
]