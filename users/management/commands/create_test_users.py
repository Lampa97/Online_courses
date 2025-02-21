from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        for i in range(1, 6):
            email = f"user_{i}@test.com"
            user = User.objects.filter(email=email).first()
            if user:
                user.delete()
            user = User.objects.create(email=email, phone_number=f"+3 050 555 00{i}", city=f"City_{i}")
            self.stdout.write(self.style.SUCCESS(f"Successfully created admin user {user.email}"))
