from django.db import models

# Create your models here.
class SerahTerima(models.Model):
    lokasi_proyek = models.CharField(max_length=255, blank=True)
    luas_total_area_proyek = models.FloatField()
    jumlah_total_unit = models.IntegerField()
    jumlah_total_unit = models.IntegerField()
    jenis_produk = models.CharField(max_length=50, blank=True)
    jumlah_tipe_rumah = models.IntegerField()
    target_pembangunan = models.IntegerField()
    verified_tipe_rumah = models.BooleanField()
    verified_jenis_psu = models.BooleanField()
    verified_data_perizinan = models.BooleanField()
    verified_admin_data_proyek = models.PositiveSmallIntegerField()
    verified_admin_tipe_rumah = models.PositiveSmallIntegerField()
    verified_admin_jenis_psu = models.PositiveSmallIntegerField()
    verified_admin_data_perizinan = models.PositiveSmallIntegerField()
    id_data_perusahaan_id = models.IntegerField()

    class Meta:
        db_table= "pelaporan_dataproyek"
