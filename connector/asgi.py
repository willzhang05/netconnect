'''***************************************************************************************
*  REFERENCES
*  Title: chatty
*  Author: SteinOveHelset
*  Date: Mar/28/21
*  URL: https://github.com/SteinOveHelset/chatty
*  URL2: https://www.youtube.com/watch?v=wLwu1NqU1rE
*
*  Title: chatty
*
***************************************************************************************'''

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "connector.settings")
django_asgi_app = get_asgi_application()

import chat.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
