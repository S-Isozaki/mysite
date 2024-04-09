from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def validate_register_data(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    validate_email(email)
    if UserModel.objects.filter(email=email).exists():
        raise ValidationError('this mail address has been used')
    if UserModel.objects.filter(username=username).exists():
        raise ValidationError('this user name has been used')
    if len(password) < 8:
        raise ValidationError('this password is too short')
    return {'email': email, 'username': username, 'password': password}

def validate_signin_data(data):
    username = data['username'].strip()
    password = data['password'].strip()
    return {'username': username, 'password': password}