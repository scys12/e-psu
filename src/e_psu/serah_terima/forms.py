from django import forms

from .models import Dokumen

class DokumenForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ("nama_psu", "perumahan", "video", "foto", "salinan_laporan")
    
    nama_psu = forms.CharField(label="Nama PSU", max_length=100)
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'video/*'}))
    foto = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))
    salinan_laporan = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}))
