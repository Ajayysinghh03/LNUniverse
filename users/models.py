from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('college_admin', 'College Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
