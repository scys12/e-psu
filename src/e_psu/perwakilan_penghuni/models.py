from django.db import models
from account.models import Account

# Create your models here.
class PerwakilanPenghuni(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE, primary_key = True)
    nama = models.CharField(max_length=30)
    alamat_rumah = models.CharField(max_length=100)

    class Meta:
        db_table= "kelola_perwakilanpenghuni"