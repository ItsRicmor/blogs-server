from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
