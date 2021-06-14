from .serializers import *
from django.shortcuts import render

# Create your views here.
import re
from django.shortcuts import render,redirect
from django.views import generic
from rest_framework.decorators import action
from .models import *
import stripe
from datetime import datetime, timedelta
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, permissions
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from verify_email.email_handler import send_verification_email

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @action(methods=['GET'], detail=False)
    def api_schema(self, request):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    @action(methods=['GET'], detail=False)
    def api_schema(self, request):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data)

class UserTaskList(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Task.objects.all()
    filterset_fields = ['user', 'task_name', 'task_id', 'task_group', 'task_priority']
    search_fields = ['user', 'task_name', 'task_description']

    @action(methods=['GET'], detail=False)
    def api_schema(self, request):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data)


