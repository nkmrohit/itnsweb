from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class feedbacks(models.Model):
    name         = models.CharField(max_length=100)
    description  = models.TextField(blank=True, max_length=200)
    link         = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='feedback/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

