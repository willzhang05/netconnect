from django.test import TestCase
from chat.apps import ChatConfig
from chat.consumers import ChatConsumer
from chat.routing import websocket_urlpatterns
from django.urls import path
from . import consumers


# Create your tests here.
class ChatTestCase(TestCase):
    def test_chat_apps(self):
        assert ChatConfig.name == 'chat'
