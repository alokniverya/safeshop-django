import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "safeshop.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="alokniverya1907@gmail.com",
        password="@devil99.com"
    )
    print("✅ Superuser created successfully.")
else:
    print("ℹ️ Superuser already exists.")
