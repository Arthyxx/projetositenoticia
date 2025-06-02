import sys
import os
import django
from django.contrib.auth import get_user_model

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define as configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportsnews.settings")
django.setup()

# Criação do superusuário
User = get_user_model()

username = "admin"
password = "admin"

if not User.objects.filter(username=username).exists():
    print("Criando superusuário...")
    User.objects.create_superuser(username=username, password=password)
    print("Superusuário criado com sucesso.")
else:
    print("Superusuário já existe.")
