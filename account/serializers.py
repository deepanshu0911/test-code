from rest_framework import serializers
from account.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('user_id', 'username', 'firstName', 'lastName', 'mobile',
        'role', 'created_date', 'is_admin', 'password')
