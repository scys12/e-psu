from django.db import models
from warga.models import Warga
from data_proyek.models import DataProyek
from django.db.models.signals import post_save

# Create your models here.
class PerwakilanPenghuni(models.Model):
    warga = models.ForeignKey(Warga, on_delete=models.CASCADE)
    data_proyek = models.ForeignKey(DataProyek, on_delete=models.CASCADE)

    class Meta:
        db_table= "kelola_perwakilanpenghuni"

    # def create_user_profile(sender, instance, created, **kwargs):  
    #     if created:            
    #         profile, created = PerwakilanPenghuni.objects.get_or_create(user=instance)

    # post_save.connect(create_user_profile, sender=Account)