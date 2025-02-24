from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig

from .views import PaymentListAPIView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments-list"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
