from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_picture = models.ImageField(verbose_name='picture', upload_to='' ,default=None ,blank=True ,null=True)
    bio = models.TextField(default='')
    phone_number = models.CharField(max_length=20, unique=True ,default='')

    def __str__(self):
        return self.username
