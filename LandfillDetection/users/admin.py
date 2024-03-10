# admin.py
from django.contrib import admin
from .models import User  # This imports the custom User model you defined

# Register your custom user model with the Django admin
admin.site.register(User)
