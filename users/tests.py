from django.test import TestCase
from .models import CustomUser
# Create your tests here.


class CustomUserTestCase(TestCase):

    def defaultValues(self):
        user1 = CustomUser()
        assert user1.politics == "U"

    def changeValue(self):
        user2 = CustomUser()
        user2.politics = "C"
        assert user2.politics == "C"

