@echo off
SETLOCAL

REM Checar se o ambiente virtual já existe
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Criando ambiente virtual...
    python -m venv venv
)

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

REM Instalar dependências
echo Instalando dependências...
pip install -r requirements.txt

REM Ir para a pasta do projeto
cd sportsnews

REM Aplicar migrações
echo Aplicando migrações...
python manage.py migrate

REM Voltar para a pasta raiz (onde está o .bat) para rodar o script do superusuário
cd ..

REM Criar superusuário se não existir
echo Verificando/criando superusuário...
python sportsnews\sportsnews\create_superuser.py

REM Voltar novamente para a pasta do projeto
cd sportsnews

REM Rodar o servidor
echo Iniciando o servidor...
python manage.py runserver

ENDLOCAL
pause
