from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Define the upload path for profile pictures
    picture = models.ImageField(upload_to='LandfillDetection/profile_pictures', blank=True, null=True)
