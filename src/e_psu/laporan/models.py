from django.db import models
from serah_terima.models import PathAndRename
from smartfields import fields
from admin_skpd.models import AdminSKPD
#Belum tau bentuk laporannya seperti apa
class BerkasLaporan(models.Model):
    tanggal_entri_laporan = models.DateField(auto_now_add=True)
    nama_psu_laporan = models.CharField(max_length=100)
    judul_laporan = models.CharField(max_length=100)
    deskripsi_laporan = models.TextField()
    foto_laporan = fields.ImageField(upload_to=PathAndRename("laporan/foto"), null=True, blank=True)
    status_laporan = models.CharField(max_length=20)
    id_admin_status_laporan = models.ForeignKey(AdminSKPD,on_delete=models.CASCADE, related_name='+',blank=True, null=True)
    bentuk_penanganan_laporan = models.TextField(null=True, blank=True)
    id_admin_penanganan_laporan = models.ForeignKey(AdminSKPD,on_delete=models.CASCADE, related_name='+',blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "kelola_berkaslaporan"