from django.db import models

from smartfields import fields

#Belum tau bentuk laporannya seperti apa
class BerkasLaporan(models.Model):
    tanggal_entri_laporan = models.DateField(auto_now_add=True)
    nama_psu_laporan = models.CharField(max_length=100)
    judul_laporan = models.CharField(max_length=100)
    deskripsi_laporan = models.CharField(max_length=200)
    foto_laporan = fields.ImageField(upload_to="laporan/foto", null=True, blank=True)
    status_laporan = models.CharField(max_length=20)
    id_admin_status_laporan = models.PositiveIntegerField(null=True, blank=True)
    bentuk_penanganan_laporan = models.TextField(null=True, blank=True)
    id_admin_penanganan_laporan = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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