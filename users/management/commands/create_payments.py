from django.core.management.base import BaseCommand
from users.models import Payment, User

class Command(BaseCommand):
    def handle(self, *args, **options):
        test_users = User.objects.filter(email__startswith="user_")

        for user in test_users:
            Payment.objects.get_or_create(user=user, amount=100, payment_method="Cash")
            Payment.objects.get_or_create(user=user, amount=2000, payment_method="Bank Transfer")
        self.stdout.write(self.style.SUCCESS("Successfully created payments for test users"))
