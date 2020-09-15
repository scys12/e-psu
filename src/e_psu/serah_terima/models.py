from django.db import models
from admin_kelola.models import AdminKelola

from smartfields import fields

class Dokumen(models.Model):
    video = fields.FileField(upload_to="serah_terima/dokumen/video/")
    foto = fields.ImageField(upload_to="serah_terima/dokumen/foto/")
    salinan_laporan = fields.FileField(upload_to="serah_terima/dokumen/salinan_laporan/")
    admin_kelola = models.OneToOneField(AdminKelola,on_delete=models.CASCADE)

    class Meta:
        db_table= "kelola_serahterima"