from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig

from .views import (PaymentCreateAPIView, PaymentListAPIView, SessionRetrieveAPIView, SubscriptionAPIView,
                    UserCreateAPIView, UserDestroyAPIView, UserListAPIView, UserRetrieveAPIView,
                    UserTokenObtainPairView, UserUpdateAPIView)

app_name = UsersConfig.name


urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments-list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment-create"),
    path("session/", SessionRetrieveAPIView.as_view(), name="session-status"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user-update"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user-delete"),
    path("login/", UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
]
