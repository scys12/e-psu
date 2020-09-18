from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Dokumen

class DokumenClearableFileInput(ClearableFileInput):
    initial_text = 'Saat ini'
    input_text = 'Ubah'
    clear_checkbox_label = 'hapus'

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

    def clean(self):
        super().clean()
        status_pengelolaan_text = self.cleaned_data.get('status_pengelolaan_text', None)
        status_pengelolaan = self.cleaned_data.get('status_pengelolaan', None)
        if not status_pengelolaan_text and not status_pengelolaan:
            self.add_error('status_pengelolaan', 'Status Pengelolaan diperlukan')
        
        pola_pengelolaan_text = self.cleaned_data.get('pola_pengelolaan_text', None)
        pola_pengelolaan = self.cleaned_data.get('pola_pengelolaan', None)
        if not pola_pengelolaan_text and not pola_pengelolaan:
            self.add_error('pola_pengelolaan', 'Pola Pengelolaan diperlukan')

        regulasi_pemanfaatan_psu_text = self.cleaned_data.get('regulasi_pemanfaatan_psu_text', None)
        regulasi_pemanfaatan_psu = self.cleaned_data.get('regulasi_pemanfaatan_psu', None)
        if not regulasi_pemanfaatan_psu_text and not regulasi_pemanfaatan_psu:
            self.add_error('regulasi_pemanfaatan_psu', 'Regulasi Pemanfaatan PSU diperlukan')

        return self.cleaned_data