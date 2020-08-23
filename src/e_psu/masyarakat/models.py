from django.db import models

# Create your models here.
class Masyarakat(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField()