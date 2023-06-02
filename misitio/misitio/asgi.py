"""
ASGI config for misitio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
# this is the configuration to run yur project as ASGI, the emerging Python standard
# for asynchronous web servers and applications

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misitio.settings')

application = get_asgi_application()
