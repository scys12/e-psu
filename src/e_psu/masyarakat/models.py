from django.db import models

# Create your models here.
class Masyarakat(models.Model):
    name = models.CharField(min_length=10, max_length=120)
    username = models.CharField(min_length=4, max_length=50)
    password = models.CharField(min_length=4,max_length=128)
    email = models.EmailField()