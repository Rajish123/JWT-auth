from django.urls import path
from .views import RegisterView,Dashboard
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('register/',RegisterView.as_view(), name = 'signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/',Dashboard.as_view(),name = 'dashboard')
]
