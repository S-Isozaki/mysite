from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.test import TestCase, Client
from django.urls import reverse

class HealthCheckTests(TestCase):
    def test_health(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "pass")

class RegistrationTests(TestCase):
    def test_builtin_register(self):
        url = reverse('register')
        # 登録
        c = Client()
        response = c.post(url, {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 201)
        response = c.post(reverse('login'), {'username': 'user1', 'password': 'password123'})
        print(response.status_code)
        print(Session.objects.all())

    def test_registration(self):
        url = reverse('register')
        # 登録
        response = self.client.post(url, {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 201)
        # 重複登録
        response = self.client.post(url, {'username': 'user1', 'email': 'user2@example.com', 'password': 'password223'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'this user name has been used')
        # パスワード
        response = self.client.post(url, {'username': 'user3', 'email': 'user3@example.com', 'password': '323'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'this password is too short')
        
        UserModel = get_user_model()
        response = self.client.post(url, {'username': 'user4  ', 'email': '  user4@example.com', 'password': ' password423 '})
        self.assertEqual(response.status_code, 201)
        
        # メールアドレス
        response = self.client.post(url, {'username': 'user5', 'email': 'example.com', 'password': 'password523'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Enter a valid email address.')
        print(UserModel.objects.count())

class AuthenticationTests(TestCase):
    def test_authentication(self):
        register_url = reverse('register')
        self.client.post(register_url, {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'})
        signin_url = reverse('signin')
        response = self.client.post(signin_url, {'username': 'user1', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        # パスワード
        response = self.client.post(signin_url, {'username': 'user1', 'password': 'password223'})
        self.assertEqual(response.status_code, 401)
        # 未登録
        response = self.client.post(signin_url, {'username': 'user2', 'password': 'password223'})
        self.assertEqual(response.status_code, 401)

class SignoutTest(TestCase):
    def test_signout(self):
        register_url = reverse('register')
        c1 = Client()
        c1.post(register_url, {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'})
        signin_url = reverse('signin')
        c1.post(signin_url, {'username': 'user1', 'password': 'password123'})

        # ユーザーのログアウト
        c2 = Client()
        c2.post(register_url, {'username': 'user2', 'email': 'user2@example.com', 'password': 'password223'})
        c2.post(signin_url, {'username': 'user2', 'password': 'password223'})
        self.assertEqual(Session.objects.count(), 2)
        print(Session.objects.all())
        # <QuerySet [<Session: mhavm5hu30iy7tlt7kef4a7e4q8c8mfr>, <Session: 08z2o1s09qfirsi17bqmb313hqi6p4ig>]>

        signout_url = reverse('signout')
        response = c2.post(signout_url)
        self.assertEqual(Session.objects.count(), 1)
        print(Session.objects.all())

        # ユーザー1としてログイン中のユーザー1がユーザー2としてログイン
        c1.post(signin_url, {'username': 'user2', 'password': 'password223'})
        print(Session.objects.all())
        # <QuerySet [<Session: 94yvceenbltq499i3p7vvcicpsy0uqh6>]>
        # 新たなセッションが発生している