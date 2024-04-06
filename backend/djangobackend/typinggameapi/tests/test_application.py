from django.test import TestCase
from django.urls import reverse

class MyApplicationTests(TestCase):
    def test_health(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "pass")