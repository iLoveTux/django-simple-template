# {{ cookiecutter.project_name }}

Welcome to your new Django project, generated from the Django Simple Template!

## Features

- Minimal dependencies: Django, Whitenoise (for static files), and CherryPy (for production server)
- Custom user model and profile
- Environment-specific settings (development and production)
- Environment variable support for secrets and configuration
- Pre-configured authentication views and templates
- Simple, classless CSS styling (easily replaceable)
- Modern, accessible navbar
- Profile editing for users
- Django 5.2+ and Python 3.13+ compatible

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv
- Git

### Setup Instructions

1. **Clone your project**
   ```bash
   git clone <your-repo-url>
   cd {{ cookiecutter.project_name }}
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # Or on Mac/Linux: source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up your database**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   set DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.dev  # On Windows
   # Or on Mac/Linux: export DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.dev
   python manage.py runserver
   ```

6. **Run the production server (CherryPy)**
   ```bash
   set DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.prod  # On Windows
   # Or on Mac/Linux: export DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.prod
   python manage.py serve
   ```
   You can configure CherryPy with environment variables (see below) or command-line arguments.

## CherryPy Server Configuration

You can control the CherryPy server using environment variables or command-line arguments:

- `CHERRYPY_HOST` (default: 127.0.0.1)
- `CHERRYPY_PORT` (default: 8000)
- `CHERRYPY_THREADS` (default: 10)
- `CHERRYPY_SSL` (default: False)
- `CHERRYPY_SSL_CERT` (path to SSL certificate)
- `CHERRYPY_SSL_KEY` (path to SSL private key)
- `CHERRYPY_AUTORELOAD` (default: False)
- `CHERRYPY_MAX_REQUESTS` (default: 0)
- `CHERRYPY_TIMEOUT` (default: 60)

Example (Windows):
```cmd
set CHERRYPY_PORT=8080
python manage.py serve
```

## Project Structure

- `settings/`: Project settings (base, dev, prod)
- `project/`: Main app (custom user, views, forms, templates)
- `templates/`: Custom templates for authentication and other views
- `static/` and `media/`: Static and media files

## Customization

- Update `settings/prod.py` for your production database and email
- Update `settings/dev.py` for your development database and email
- Add fields to registration/profile in `project/forms.py`
- Swap the Bahunya CSS in `base.html` for your own style

## Security Notes

- All forms use `csrf_token` for CSRF protection.
- Logout is POST-only
- No sensitive data is included in the repository

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
