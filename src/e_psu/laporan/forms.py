from django import forms

from .models import BerkasLaporan

class BerkasLaporanForm(forms.ModelForm):
    class Meta:
        model = BerkasLaporan
        fields = ("nama_psu", "perumahan", "judul_laporan",
            "deskripsi_laporan", "bukti_foto_laporan", "bukti_video_laporan")

    nama_psu = forms.CharField(label="Nama PSU", max_length=100)
    perumahan = forms.CharField(label="Perumahan", max_length=100)
    judul_laporan = forms.CharField(label="Judul Laporan", max_length=100)
    deskripsi_laporan = forms.CharField()
    bukti_foto_laporan = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    bukti_video_laporan = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'video/*'}))
