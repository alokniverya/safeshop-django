import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "safeshop.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(email="alokniverya1907@gmail.com").exists():
    User.objects.create_superuser(
        email="alokniverya1907@gmail.com",
        username="admin",
        first_name="Alok",
        last_name="Singh",
        password="@devil99.com"
    )
    print("✅ Superuser created successfully.")
else:
    print("ℹ️ Superuser already exists.")
