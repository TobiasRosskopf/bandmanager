import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_start(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
