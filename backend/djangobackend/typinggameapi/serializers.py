from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import AppUser, UserRecord

UserModel = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, clean_data):
        user = UserModel.objects.create_user(username=clean_data['username'], email=clean_data['email'], password=clean_data['password'])
        user.save()
        return user

class UserRecordSerializer(serializers.ModelSerializer):
    user_name = User
    elapsed_time = serializers.DecimalField(max_digits=5, decimal_places=2)
    word_length = serializers.IntegerField()
    class Meta:
        model = UserRecord
        fields = ['user_name', 'elapsed_time', 'word_length']