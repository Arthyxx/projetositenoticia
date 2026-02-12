# Red Zone

**Red Zone** is a sports news website focused on American sports, including American football, basketball, baseball, and hockey.

## Features

- News organized by category  
- Image upload support  
- Administrative panel via Django Admin  
- Responsive design  

## Technologies

- [Python 3](https://www.python.org/)
- [Django 5.2.1](https://www.djangoproject.com/)
- [Pillow 11.2.1](https://pillow.readthedocs.io/en/stable/)
- [SQLParse](https://pypi.org/project/sqlparse/)
- [Tzdata](https://pypi.org/project/tzdata/)

## How to Run

### Using `.bat`

Double-click **`iniciar_servidor.bat`** to start the local server.  
The website will be available at:  
`http://127.0.0.1:8000/`

Use the shortcut **`Redzone ADM.url`** to access the admin panel directly:  
`http://127.0.0.1:8000/login/?next=/admin-dashboard/`

### Manual Setup

```bash
git clone https://github.com/YOUR-USERNAME/redzone.git
cd redzone
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Usage

Access `http://127.0.0.1:8000/` and browse the news categories.

Administration is available at:  
`http://127.0.0.1:8000/admin` or via the provided shortcut.

## Team

- Antonio Israel  
- Arthur Gonçalves  
- Gabriel Miranda  
- Jonas Rego  
- Roberto Talysson  
- Suan Eden  

Course: Web Development with HTML, CSS, JavaScript, and PHP — Estácio

## License

MIT License.
