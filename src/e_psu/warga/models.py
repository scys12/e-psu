from django.db import models
from account.models import Account
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
# Create your models here.
class Warga(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE, primary_key = True)
    no_ktp = models.CharField(validators=[RegexValidator(regex='\d{16}$', message='KTP harus mempunyai 16 digit angka')], unique=True, max_length=16)
    nama = models.CharField(max_length=30)
    alamat_rumah = models.CharField(max_length=100)

    class Meta:
        db_table= "kelola_warga"
    
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:            
            profile, created = Warga.objects.get_or_create(user=instance)

    post_save.connect(create_user_profile, sender=Account)