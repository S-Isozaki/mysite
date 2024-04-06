from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

UserModel = get_user_model()
user_obj = UserModel.objects

class MyModelTests(TestCase):
    def test_create_user(self):

        # ユーザー登録
        self.assertEqual(user_obj.count(), 0)
        u = user_obj.create_user('user1', 'user1@example.com', 'password1')
        self.assertEqual(user_obj.count(), 0)
        u.save()
        self.assertEqual(user_obj.count(), 1)
        self.assertEqual(u.user_id, 1)
        self.assertIsNotNone(user_obj.get(username='user1'))
        with self.assertRaises(UserModel.DoesNotExist):
            user_obj.get(username='user2')
        
        # 登録情報の不足
        with self.assertRaises(ValueError):
            u = user_obj.create_user(username='user2', email='user2@example.com')
        
        # 重複登録
        with self.assertRaises(ValidationError):
            u = user_obj.create_user('user1', 'user2@example.com', 'password2')

    def test_delete_user(self):
        u = user_obj.create_user('user1', 'user1@example.com', 'password1')
        u.save()
        self.assertTrue(user_obj.filter(username='user1').exists())

        # ユーザー情報の削除
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
    
    def test_permit_user(self):
        client1 = user_obj.create_user(username='user1', email='user1@example.com', password='password1')

    def test_add_record(self):
        user1 = user_obj.create_user(username='user1', email='user1@example.com', password='password1')