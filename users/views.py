from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, views
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from education.models import Course

from .models import Payment, Subscription, User
from .permissions import IsAdmin, IsOwner
from .serializers import (OtherUserSerializer, PaymentSerializer, SubscriptionSerializer, UserSerializer,
                          UserTokenObtainPairSerializer)
from .services import check_session_status, create_stripe_price, create_stripe_product, create_stripe_session


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = OtherUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.is_active = True
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner,)


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.get_object() == self.request.user:
            return UserSerializer
        return OtherUserSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["payment_method", "paid_course", "paid_lesson"]
    ordering_fields = ["payment_date"]


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product = payment.paid_course or payment.paid_lesson
        product_name = create_stripe_product(product)
        price = create_stripe_price(payment.amount, product_name)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class SessionRetrieveAPIView(views.APIView):
    def get(self, request):
        session_id = request.data.get("session_id")
        session_status = check_session_status(session_id)
        return Response({"session_status": session_status})


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data["email"])
        user.last_login = timezone.now()
        user.save()
        return response


class SubscriptionAPIView(views.APIView):

    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.data.get("user")
        user = get_object_or_404(User, pk=user)
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Deleted subscription"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Added subscription"
        return Response({"message": message})
