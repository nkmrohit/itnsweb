from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField  

# Create your models here.
class settings(models.Model):
    logo = models.ImageField(blank=True,upload_to='setting/')
    tagline         = models.CharField(max_length=50)
    favicon = models.ImageField(blank=True,upload_to='setting/')
    name         = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    seo  = HTMLField()
    meta  = HTMLField()
    footerContent  = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

