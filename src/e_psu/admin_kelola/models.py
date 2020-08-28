from django.db import models
from account.models import Account
# Create your models here.
class AdminKelola(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE, primary_key = True)
    nama = models.CharField(max_length=30)

    class Meta:
        db_table= "kelola_adminkelola"