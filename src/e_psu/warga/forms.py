from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.validators import MinLengthValidator

from .models import Warga
    
class WargaRegistrationForm(forms.ModelForm):    
    class Meta:
        model = Warga
        fields = ['no_ktp', 'nama', 'alamat_rumah']

    def clean_password(self):
        user_data = self.cleaned_data
        print(user_data)
        if user_data['password'] != user_data['konfirmasi_password']:
            return forms.ValidationError("Password tidak sama")

        return user_data['password']