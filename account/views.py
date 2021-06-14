from django.shortcuts import render

# Create your views here.
import re
from django.shortcuts import render,redirect
from rest_framework import generics
from .models import *
import stripe
from datetime import datetime, timedelta
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, permissions
from .serializers import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMessage
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = AccountSerializer
    queryset = User.objects.all()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterSerializer