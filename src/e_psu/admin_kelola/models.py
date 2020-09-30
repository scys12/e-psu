from django.db import models
from account.models import Account
from django.db.models.signals import post_save
# Create your models here.
class AdminKelola(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    nama = models.CharField(max_length=30)

    class Meta:
        db_table= "kelola_adminkelola"
    
    # def create_user_profile(sender, instance, created, raw=False, **kwargs):
    #     if created and not raw:
    #         profile = AdminKelola.objects.create(user=instance)
    
    # post_save.connect(create_user_profile, sender=Account)