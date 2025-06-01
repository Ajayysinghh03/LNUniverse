from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('college_admin', 'College Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        blank=True
    )
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Fields for college admin, teachers, and students
    college = models.ForeignKey('colleges.College', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
