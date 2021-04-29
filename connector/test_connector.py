from django.test import TestCase
from connector.wsgi import application as application_wsgi
from connector.asgi import application as application_asgi
import os
from django.core.wsgi import get_wsgi_application




#Create your tests here.
class ChatTestCase(TestCase):

    # I know, not the best test, but the result is different each time.
    def test_wsgi_field(self):
        assert (application_wsgi != None) and (application_wsgi != get_wsgi_application()) and (get_wsgi_application()!= None)

    # I know, not the best test, but it is hard to test anything else on this one.
    def test_asgi_field(self):
        print (application_asgi)
        assert application_asgi != None

