from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Dokumen

class DokumenClearableFileInput(ClearableFileInput):
    initial_text = 'Saat ini'
    input_text = 'Ubah'

class DokumenForm(forms.ModelForm):
    class Media:
        js = ['js/serah_terima.js']

    class Meta:
        model = Dokumen
        exclude = ['admin_kelola',]

    video = forms.FileField(widget=DokumenClearableFileInput(attrs={'accept': 'video/*'}))
    foto = forms.ImageField(widget=DokumenClearableFileInput(attrs={'accept': 'image/*'}))
    salinan_laporan = forms.FileField(widget=DokumenClearableFileInput(attrs={'accept': 'application/pdf'}))
    status_pengelolaan_text = forms.CharField(required=False,label="Status Pengelolaan", max_length=100)
    pola_pengelolaan_text = forms.CharField(required=False,label="Pola Pengelolaan", max_length=100)
    regulasi_pemanfaatan_psu_text = forms.CharField(required=False,label="Regulasi Pemanfaatan PSU", max_length=100)
    status_pengelolaan = forms.FileField(required=False,widget=DokumenClearableFileInput(attrs={'accept': 'application/pdf'}))
    pola_pengelolaan = forms.FileField(required=False,widget=DokumenClearableFileInput(attrs={'accept': 'application/pdf'}))
    regulasi_pemanfaatan_psu = forms.FileField(required=False,widget=DokumenClearableFileInput(attrs={'accept': 'application/pdf'}))
