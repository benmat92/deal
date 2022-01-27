from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy


class CustomUser(AbstractUser):
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    # add additional fields in here
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']
    def __str__(self):
        return self.username

# Create your models here.
