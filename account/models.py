from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from phone_field import PhoneField
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone and not email:
            raise ValueError('Users must have either an email or a phone number')

        user = self.model(
            phone = phone,
            email = email, 
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email = email,
            phone = phone,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        primary_key=True
    )
    phone = models.CharField(verbose_name='Phone Number', unique=True, max_length= 10)
    first_name = models.CharField(verbose_name='First Name', max_length= 20)
    last_name = models.CharField(verbose_name='Last Name', max_length = 20)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.first_name

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin