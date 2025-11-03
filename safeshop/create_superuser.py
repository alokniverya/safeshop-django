from django.contrib.auth import get_user_model

User = get_user_model()

try:
    if not User.objects.filter(email="alokniverya1907@gmail.com").exists():
        User.objects.create_superuser(
            first_name="Alok",
            last_name="Singh",
            username="admin",
            email="alokniverya1907@gmail.com",
            password="devil99.com"
        )
        print("✅ Superuser created successfully!")
    else:
        print("⚠️ Superuser already exists.")
except Exception as e:
    print("❌ Superuser creation failed:", e)
