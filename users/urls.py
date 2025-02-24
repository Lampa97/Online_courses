from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from .views import PaymentListAPIView, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, UserTokenObtainPairView

app_name = UsersConfig.name


urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments-list"),
    path("register/", UserListCreateAPIView.as_view(), name="register"),
    path("users/", UserListCreateAPIView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user-update"),
    path("user/<int:pk>/delete/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user-delete"),
    path("login/", UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
