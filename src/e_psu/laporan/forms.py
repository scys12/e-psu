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

    nama_psu_laporan = forms.CharField(label="Nama PSU", max_length=100)
    judul_laporan = forms.CharField(label="Judul Laporan", max_length=100)
    deskripsi_laporan = forms.CharField(widget=forms.Textarea,label="Deskripsi Laporan")
    foto_laporan = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}), required=False)

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = BerkasLaporan
        fields = ("status_laporan",)
    
    status_laporan_choices = [
        ('BELUM', 'Belum Diproses'),
        ('SEDANG', 'Sedang Diproses'),
        ('SELESAI', 'Selesai Diproses')
    ]
    status_laporan = forms.ChoiceField(widget=forms.RadioSelect, choices=status_laporan_choices, label="Status Laporan")

class UpdatePenangananForm(forms.ModelForm):
    class Meta:
        model = BerkasLaporan
        fields = ("bentuk_penanganan_laporan",)

    bentuk_penanganan_laporan = forms.CharField(widget=forms.Textarea, label="Penanganan Terhadap Laporan")