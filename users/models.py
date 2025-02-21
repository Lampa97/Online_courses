from django.contrib.auth.models import AbstractUser
from django.db import models
from education.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone_number")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="City")
    avatar = models.ImageField(
        upload_to="avatars/", default="avatars/default_avatar.jpg", blank=True, null=True, verbose_name="Avatar"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = [
            "email",
        ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ("Cash", "Cash"),
        ("Bank Transfer", "Bank Transfer"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments", verbose_name="Payment")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Payment date")
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True, related_name="payments", verbose_name="Paid course")
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, related_name="payments", verbose_name="Paid lesson")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="Payment method")
