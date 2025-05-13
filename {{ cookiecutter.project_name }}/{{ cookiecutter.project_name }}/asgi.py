"""
ASGI config for {{ cookiecutter.project_name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

# Set default settings module if not already set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.project_name }}.settings.prod')

from django.core.asgi import get_asgi_application

application = get_asgi_application()
