from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserRecord

class UserRecordSerializer(serializers.ModelSerializer):
    user_name = User
    elapsed_time = serializers.DecimalField(max_digits=5, decimal_places=2)
    word_length = serializers.IntegerField()
    class Meta:
        model = UserRecord
        fields = ['user_name', 'elapsed_time', 'word_length']