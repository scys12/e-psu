from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.validators import MinLengthValidator

from .models import Warga
    
class WargaRegistrationForm(forms.ModelForm):    
    class Meta:
        model = Warga
        fields = ['no_ktp', 'nama', 'alamat_rumah']