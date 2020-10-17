from django.db import models

# Create your models here.
class DataPerusahaan(models.Model):
    id_data_perusahaan = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nama_perusahaan = models.CharField(max_length=255)
    akta_pendirian_badan_usaha = models.FileField(upload_to='akta_pendirian_badan_usaha')
    nama_pemilik = models.CharField(max_length=255)
    foto_pemilik = models.ImageField(upload_to='foto_pemilik')
    ktp_pemilik = models.FileField(upload_to='ktp_pemilik')
    bentuk_perusahaan = models.CharField(max_length=20)
    alamat_perusahaan = models.CharField(max_length=255)
    tahun_berdiri = models.IntegerField()
    no_telp = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.CharField(max_length=255)
    verified_admin = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table= "pelaporan_dataperusahaan"

class DataProyek(models.Model):
    id_data_proyek = models.AutoField(primary_key=True)
    id_data_perusahaan = models.ForeignKey(DataPerusahaan, on_delete=models.CASCADE)
    lokasi_proyek = models.CharField(max_length=255)
    luas_total_area_proyek = models.FloatField()
    jumlah_total_unit = models.IntegerField()
    jenis_produk = models.CharField(max_length=50)
    jumlah_tipe_rumah = models.IntegerField()
    target_pembangunan = models.IntegerField()
    verified_tipe_rumah = models.BooleanField(default=False)
    verified_jenis_psu = models.BooleanField(default=False)
    verified_data_perizinan = models.BooleanField(default=False)
    verified_admin_data_proyek = models.PositiveSmallIntegerField(default=0)
    verified_admin_tipe_rumah = models.PositiveSmallIntegerField(default=0)
    verified_admin_jenis_psu = models.PositiveSmallIntegerField(default=0)
    verified_admin_data_perizinan = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table= "pelaporan_dataproyek"

    def __str__(self):
        return self.lokasi_proyek