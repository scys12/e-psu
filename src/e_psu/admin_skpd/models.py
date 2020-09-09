from django.db import models
from account.models import Account
from django.db.models.signals import post_save
# Create your models here.
class AdminSKPD(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE, primary_key = True)
    nama = models.CharField(max_length=30)

    class Meta:
        db_table= "kelola_adminskpd"
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = AdminSKPD.objects.get_or_create(user=instance)
    
    post_save.connect(create_user_profile, sender=Account)