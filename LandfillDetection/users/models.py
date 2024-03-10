# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from pictures.models import PictureField

# Create your custom user model here.
class User(AbstractUser):
    picture = PictureField(upload_to='LandfillDetection/profile_pictures', blank=True, null=True)

