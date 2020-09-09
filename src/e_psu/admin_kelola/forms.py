from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.validators import MinLengthValidator

from .models import AdminKelola
    
class AdminKelolaRegistrationForm(forms.ModelForm):    
    class Meta:
        model = AdminKelola
        fields = ['nama']