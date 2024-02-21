from django.db import models
from blog.models import Blog

# Create your models here.

class Series(models.Model):
    title = models.CharField(max_length=100)
    blogs = models.ManyToManyField(Blog)