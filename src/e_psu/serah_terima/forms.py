from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Dokumen

class DokumenClearableFileInput(ClearableFileInput):
    initial_text = 'Saat ini'
    input_text = 'Ubah'

class DokumenForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = "__all__"

    nama_psu = forms.CharField(label="Nama PSU", max_length=100)
    video = forms.FileField(widget=DokumenClearableFileInput(attrs={'accept': 'video/*'}))
    foto = forms.ImageField(widget=DokumenClearableFileInput(attrs={'accept': 'image/*'}))
    salinan_laporan = forms.FileField(widget=DokumenClearableFileInput(attrs={'accept': 'application/pdf'}))
