from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError

class MyApplicationTests(TestCase):
    def test_health(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "pass")

    def test_registration(self):
        url = reverse('register')
        response = self.client.post(url, {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 201)
        response = self.client.post(url, {'username': 'user1', 'email': 'user2@example.com', 'password': 'password223'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post(url, {'username': 'user3', 'email': 'user3@example.com', 'password': '323'})
        self.assertEqual(response.status_code, 400)