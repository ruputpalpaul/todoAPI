from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from account.models import User

TASKGROUPS = [
    ('H', 'Home'),
    ('W', 'Work'),
    ('P', 'Personal'),
    ('F', 'Family'),
]

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram = models.URLField(max_length=400, blank=True, null=True)
    pinterest = models.URLField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=100, primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = RichTextField()
    task_priority = models.IntegerField(default=0)
    task_image = models.ImageField(upload_to='task', null=True, blank=True)
    task_group = models.CharField(max_length=100, choices=TASKGROUPS)

    def __str__(self):
        return self.task_name

