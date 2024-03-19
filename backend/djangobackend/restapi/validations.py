from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def validate_register_data(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    if UserModel.objects.filter(email=email).exists():
        raise ValidationError('this mail address has been used')
    if UserModel.objects.filter(username=username).exists():
        raise ValidationError('this user name has been used')
    return data