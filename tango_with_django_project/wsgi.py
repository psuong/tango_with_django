"""
WSGI config for tango_with_django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# wsgi.py, a Python script used to help run your development server and deploy your project to a production environment.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

application = get_wsgi_application()
