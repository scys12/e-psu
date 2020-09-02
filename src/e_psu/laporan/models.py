from django.db import models

from smartfields import fields

#Belum tau bentuk laporannya seperti apa
class BerkasLaporan(models.Model):
    tanggal_entri_laporan = models.DateField()
    deskripsi_laporan = models.CharField(max_length=200)
    foto_laporan = fields.ImageField(upload_to="laporan/foto", null=True, blank=True)
    status_laporan = models.CharField(max_length=20)
    id_admin_status_laporan = models.CharField(max_length=20)
    bentuk_penanganan_laporan = models.TextField()
    id_admin_penanganan_laporan = models.CharField(max_length=20)


    # nama_psu = models.CharField(max_length=100)
    # perumahan = models.CharField(max_length=100)
    # judul_laporan = models.CharField(max_length=100)
    # deskripsi_laporan = models.TextField(null=False, blank=False)
    # bukti_foto_laporan = fields.ImageField(upload_to="laporan/foto",
    #     null=True, blank=True)
    # bukti_video_laporan = fields.FileField(upload_to="laporan/video",
    #     null=True, blank=True)

    class Meta:
        db_table = "kelola_berkaslaporan"