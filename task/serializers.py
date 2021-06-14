from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'task_description']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'