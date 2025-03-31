from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    # Adding unique related_name to avoid clash with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',  # Change the related_name here
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_set_custom',  # Change the related_name here
        blank=True
    )
