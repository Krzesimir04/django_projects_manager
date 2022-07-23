from django.test import TestCase, Client
from .views import *
# Create your tests here.

class Test_views(TestCase):
    def test_index(self):
        client=Client()
        request=client.get('/')
        self.assertEqual(request.status_code, 200)
