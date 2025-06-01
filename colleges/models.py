from django.db import models
from django.core.validators import RegexValidator

class College(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(regex=r'^[A-Z0-9]{3,10}$')],
        help_text="Unique college code (3-10 characters, uppercase letters and numbers only)"
    )
    address = models.TextField()
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]
    )
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True)
    established_year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'Colleges'
        ordering = ['name']
