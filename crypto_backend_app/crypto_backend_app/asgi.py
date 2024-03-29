"""
ASGI config for crypto_backend_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crypto_backend_app.settings")
django_asgi_app = get_asgi_application()

import data_streaming.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(data_streaming.routing.websocket_urlpatterns))
        ),
    }
)

