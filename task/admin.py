from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User
# Register your models here.



admin.site.register(Task)
admin.site.register(Profile)