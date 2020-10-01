from django.db import models
from admin_kelola.models import AdminKelola
from smartfields import fields
from e_psu.helpers import PathAndRename
class Dokumen(models.Model):
    video = fields.FileField(upload_to=PathAndRename("serah_terima/dokumen/video/"))
    foto = fields.ImageField(upload_to=PathAndRename("serah_terima/dokumen/foto/"))
    salinan_laporan = fields.FileField(upload_to=PathAndRename("serah_terima/dokumen/salinan_laporan/"))
    admin_kelola = models.ForeignKey(AdminKelola,on_delete=models.CASCADE)
    status_pengelolaan_text = models.CharField(max_length=100, blank=True)
    pola_pengelolaan_text = models.CharField(max_length=100, blank=True)
    regulasi_pemanfaatan_psu_text = models.CharField(max_length=100,blank=True)
    status_pengelolaan = fields.FileField(upload_to=PathAndRename("serah_terima/dokumen/status_pengelolaan/"),blank=True, null=True)
    pola_pengelolaan = fields.FileField(upload_to=PathAndRename("serah_terima/dokumen/pola_pengelolaan/"),blank=True, null=True)
    regulasi_pemanfaatan_psu = fields.FileField(upload_to=PathAndRename("serah_terima/dokumen/regulasi_pemanfaatan_psu/"),blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "kelola_serahterima"