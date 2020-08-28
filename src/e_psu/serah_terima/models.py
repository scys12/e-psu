from django.db import models

from smartfields import fields

class Dokumen(models.Model):
    nama_psu = models.CharField(max_length=100)
    perumahan = models.CharField(max_length=100)
    video = fields.FileField(upload_to="serah_terima/dokumen/video/")
    foto = fields.ImageField(upload_to="serah_terima/dokumen/foto/")
    salinan_laporan = fields.FileField(upload_to="serah_terima/dokumen/salinan_laporan/")

    class Meta:
        db_table= "kelola_serahterima"