from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class portfolios(models.Model):
    name         = models.CharField(max_length=100)
    description  = models.TextField(blank=True, max_length=200)
    image = models.ImageField(blank=True,upload_to='portfolio/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


