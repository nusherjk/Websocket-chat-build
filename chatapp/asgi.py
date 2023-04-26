"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')
#
# application = get_asgi_application()


# mysite/asgi.py
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter # added protocoltype router in channels integration
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application



import chat.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(chat.routing.websocket_urlpatterns)
            )
        ),
        # Just HTTP for now. (We can add other protocols later.)
    }
)