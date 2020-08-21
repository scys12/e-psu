from django.db import models

from smartfields import fields

#Belum tau bentuk laporannya seperti apa
class BerkasLaporan(models.Model):
    nama_psu = models.CharField(max_length=100)
    perumahan = models.CharField(max_length=100)
    judul_laporan = models.CharField(max_length=100)
    deskripsi_laporan = models.TextField(null=False, blank=False)
    bukti_foto_laporan = fields.ImageField(upload_to="laporan/foto",
        null=True, blank=True)
    bukti_video_laporan = fields.FileField(upload_to="laporan/video",
        null=True, blank=True)