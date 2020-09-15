from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Dokumen

class DokumenClearableFileInput(ClearableFileInput):
    initial_text = 'Saat ini'
    input_text = 'Ubah'

class DokumenForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        exclude = ['admin_kelola']

    video = forms.FileField(widget=DokumenClearableFileInput(attrs={'accept': 'video/*'}))
    foto = forms.ImageField(widget=DokumenClearableFileInput(attrs={'accept': 'image/*'}))
    salinan_laporan = forms.FileField(widget=DokumenClearableFileInput(attrs={'accept': 'application/pdf'}))
