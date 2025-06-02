import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportsnews.settings")
django.setup()

User = get_user_model()

username = "admin"
email = "silveirasuan@gmail.com"
password = "admin"

if not User.objects.filter(username=username).exists():
    print("Criando superusuário...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superusuário criado com sucesso.")
else:
    print("Superusuário já existe.")
    