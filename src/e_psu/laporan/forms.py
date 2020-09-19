from django import forms
from django.forms.widgets import ClearableFileInput

from .models import BerkasLaporan

class BerkasLaporanClearableFileInput(ClearableFileInput):
    initial_text = 'Saat ini'
    input_text = 'Ubah'

class BerkasLaporanForm(forms.ModelForm):
    class Meta:
        model = BerkasLaporan
        fields = ("nama_psu_laporan", "judul_laporan", "deskripsi_laporan", "foto_laporan",)
        # fields = "__all__"
        # fields = ("nama_psu", "perumahan", "judul_laporan",
        #     "deskripsi_laporan", "bukti_foto_laporan", "bukti_video_laporan")

    nama_psu_laporan = forms.CharField(label="Nama PSU", max_length=100)
    judul_laporan = forms.CharField(label="Judul Laporan", max_length=100)
    deskripsi_laporan = forms.CharField(label="Deskripsi Laporan")
    foto_laporan = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}), required=False)
    # nama_psu = forms.CharField(label="Nama PSU", max_length=100)
    # perumahan = forms.CharField(label="Perumahan", max_length=100)
    # judul_laporan = forms.CharField(label="Judul Laporan", max_length=100)
    # deskripsi_laporan = forms.CharField()
    # bukti_foto_laporan = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}), required=False)
    # bukti_video_laporan = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'video/*'}), required=False)
