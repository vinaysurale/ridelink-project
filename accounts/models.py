# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='passenger')
    
    # Add these two lines to fix the error
    groups = models.ManyToManyField('auth.Group', related_name='account_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='account_user_permissions', blank=True)