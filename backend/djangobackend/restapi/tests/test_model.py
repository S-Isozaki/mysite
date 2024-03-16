from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

UserModel = get_user_model()
user_obj = UserModel.objects

class MyModelTests(TestCase):
    def test_create_user(self):
        self.assertEqual(user_obj.count(), 0)
        u = user_obj.create_user('user1', 'user1@example.com', 'password1')
        self.assertEqual(user_obj.count(), 0)
        u.save()
        self.assertEqual(user_obj.count(), 1)
        self.assertIsNotNone(user_obj.get(username='user1'))
        with self.assertRaises(UserModel.DoesNotExist):
            user_obj.get(username='user2')

    def test_delete_user(self):
        u = user_obj.create_user('user1', 'user1@example.com', 'password1')
        u.save()
        u.delete()
        self.assertEqual(user_obj.count(), 0)
        with self.assertRaises(UserModel.DoesNotExist):
            user_obj.get(username='user1')

    def test_authenticate_user(self):
        client1 = user_obj.create_user('user1', email='user1@example.com', password='password1')
        client1.save()
        user1 = authenticate(username='user1', password='password1')
        self.assertEqual(user1.get_username(), 'user1')
        client2 = authenticate(username='user1', password='')
        self.assertIsNone(client2)

    def test_add_record(self):
        user1 = user_obj.create_user(username='user1', email='user1@example.com', password='password1')