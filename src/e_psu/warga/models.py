from django.db import models
from account.models import Account
# Create your models here.
class Warga(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE, primary_key = True, related_name="Warga")
    no_ktp = models.CharField(max_length=16)
    nama = models.CharField(max_length=30)
    alamat_rumah = models.CharField(max_length=100)

    class Meta:
        db_table= "kelola_warga"