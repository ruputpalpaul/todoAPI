from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'date_of_birth', 'is_admin']
