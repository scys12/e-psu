from django import forms

from .models import PerwakilanPenghuni

class PerwakilanPenghuniForm(forms.ModelForm):
    class Meta:
        model = PerwakilanPenghuni
        exclude = ['user',]