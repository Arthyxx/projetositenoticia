# Red Zone

**Red Zone** é um site de notícias sobre esportes americanos, focado em futebol americano, basquete, baseball e hóquei.

## Funcionalidades

- Notícias por categoria  
- Upload de imagens  
- Painel administrativo via Django Admin  
- Design responsivo

## Tecnologias

- [Python 3]([url](https://www.python.org/))
- D[jango 5.2.1]([url](https://www.djangoproject.com/))
- [Pillow 11.2.1]([url](https://pillow.readthedocs.io/en/stable/))
- [SQLParse]([url](https://pypi.org/project/sqlparse/))  
- [Tzdata]([url](https://pypi.org/project/tzdata/))

## Como rodar

### Usando `.bat`

Clique duas vezes em **`iniciar_servidor.bat`** para rodar o servidor local.  
O site abrirá em `http://127.0.0.1:8000/`.

Use o atalho **`Redzone ADM.url`** para acessar o admin direto:  
`http://127.0.0.1:8000/login/?next=/admin-dashboard/`

### Manual

```bash
git clone https://github.com/SEU-USUARIO/redzone.git
cd redzone
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Uso

Acesse `http://127.0.0.1:8000/` e navegue pelas categorias.

Administração via `http://127.0.0.1:8000/admin` ou atalho indicado.

## Equipe

- Antonio Israel  
- Arthur Gonçalves  
- Gabriel Miranda  
- Jonas Rego  
- Roberto Talysson  
- Suan Eden

Curso: Desenvolvimento Web em HTML, CSS, JavaScript e PHP — Estácio

## Licença

Licença MIT.
