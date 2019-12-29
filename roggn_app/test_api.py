import unittest
from django.test import Client

from .models import Gig

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        Gig.objects.create(date="2019-06-07", location="Rock am Ring")

    def test_get(self):
        json_answer = """
            {
                "date": "2019-06-07",
                "event": "",
                "id": 1,
                "location": "Rock am Ring",
                "resource_uri": "/api/gig/1/",
                "time": "00:00:00"
            }
        """
        response = self.client.get('/api/gig/1')
        print(response)
        self.assertEqual(response.content, json_answer)
