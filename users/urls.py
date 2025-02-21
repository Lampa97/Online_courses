from rest_framework.routers import DefaultRouter
from django.urls import path
from users.apps import UsersConfig

from .views import UserViewSet, PaymentListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
path("payments/", PaymentListAPIView.as_view(), name="payments-list"),
]

urlpatterns += router.urls
