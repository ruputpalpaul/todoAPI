from django.shortcuts import render

# Create your views here.
import re
from django.shortcuts import render,redirect
from .models import *
import stripe
from datetime import datetime, timedelta
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, permissions
from .serializers import *
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = AccountSerializer
    queryset = User.objects.all()