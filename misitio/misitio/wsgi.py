"""
WSGI config for misitio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
# this is the configuration to run your project as a Web Server Gateway Interface (WSGI)
# application.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misitio.settings')

application = get_wsgi_application()
