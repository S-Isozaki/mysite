from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User

class AppUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('A username is required')
        if not email:
            raise ValueError('A mail address is required')
        if not password:
            raise ValueError('A password is required')
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save
        return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = AppUserManager()

class UserRecord(models.Model):
    user_name = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    elapsed_time = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    word_length = models.PositiveIntegerField()