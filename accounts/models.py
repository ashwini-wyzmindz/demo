from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,Permission

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username
    