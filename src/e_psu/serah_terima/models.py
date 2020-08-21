from django.db import models

class Dokumen(models.Model):
    nama_psu = models.CharField(max_length=100)
    perumahan = models.CharField(max_length=100)
    video = models.FileField(upload_to="serah_terima/dokumen/video/")
    foto = models.ImageField(upload_to="serah_terima/dokumen/foto/")
    salinan_laporan = models.FileField(upload_to="serah_terima/dokumen/salinan_laporan/")