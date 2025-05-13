# Django Simple Template

Welcome to the **Django Simple Template**, a minimal and "future-proof" Django project template with very few dependencies. This template is designed to help you quickly start a new Django project with sensible defaults and essential features.

* "Future proof" isn't a guarantee, there are just very minimal dependencies (just django, whitenoise and CherryPy).

## Features

- **Minimal Dependencies**: Only includes Django, Whitenoise for serving static files and CherryPy for a TLS enabled production-ready web server.
- **Custom User Model**: A custom user model is pre-configured for flexibility.
- **Environment-Specific Settings**: Separate settings for development and production environments.
- **Environment Variable Support**: Easily override settings like `DJANGO_SECRET_KEY` and `DJANGO_DEBUG` using environment variables. `DJANGO_SETTINGS_MODULE` environment variable is required and can be `{{project_name}}.settings.dev` or `{{project_name}}.settings.prod` (replace `{{project_name}}` with the name of your project).
- **Static and Media File Handling**: Configured to serve static and media files with Whitenoise.
- **Authentication Views**: Pre-configured login, logout, password reset, and profile views with custom templates.
- **Logging**: Verbose logging in development and warning-level logging in production.
- **Email Configuration**: File-based email backend by default, with a sample Gmail SMTP configuration.
- **Simple Styling**: All styling is through a single [classless CSS stylesheet](https://github.com/Kimeiga/bahunya). You can replace it or extend it.
- **Modern Navbar**: Responsive, accessible navbar with SVG user icon and dropdown for authenticated users.
- **Profile Editing**: Users can edit their profile after registration.
- **Django 5.2+ and Python 3.13+ Compatible**: Tested with the latest Django and Python versions.
- **Automation Scripts**: Includes sample scripts and one-liners for automating Cookiecutter project generation (Python, Bash, Windows CMD).

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv
- Git
- Cookiecutter

### Generating a New Project

1. Install Cookiecutter if you don't already have it:
   ```bash
   pip install cookiecutter
   ```

2. Use this template to generate a new project:
   ```bash
   cookiecutter https://github.com/ilovetux/django-simple-template.git
   ```

3. Follow the prompts to provide a project name.

4. Navigate to your new project directory (replace myproject with your project name):
   ```bash
   cd myproject
   ```

5. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

6. Run the development server:
   ```bash
   export DJANGO_SETTINGS_MODULE=myproject.settings.dev # On Windows: set DJANGO_SETTINGS_MODULE=myproject.settings.dev
   python manage.py runserver
   ```

7. Run the production server:
   ```bash
   export DJANGO_SETTINGS_MODULE=myproject.settings.prod # On Windows: set DJANGO_SETTINGS_MODULE=myproject.settings.prod
   python manage.py serve
   ```

### Project Structure

- `settings/`: Contains `base.py` (shared settings), `dev.py` (development settings), and `prod.py` (production settings).
- `project/`: Contains the main app with custom user model, views, and templates.
- `projects/templates/`: Includes custom templates for authentication and other views.
- `static/` and `media/`: Directories for static and media files.

### Customization

- Update `settings/prod.py` with your production database and email configurations.
- Update `settings/dev.py` with you development database and email configuration
- Add additional apps or features as needed.
- To add more fields to registration or profile, update `CustomUserCreationForm` and `UserProfileForm` in `project/forms.py`.
- To use a different CSS framework, swap the Bahunya CDN link in `base.html`.

## Security Notes

- All forms use `{% csrf_token %}` for CSRF protection.
- Logout is POST-only for security.
- No sensitive data is included in the repository.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.