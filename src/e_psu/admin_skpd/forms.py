from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.validators import MinLengthValidator

from .models import AdminSKPD
    
class AdminSKPDRegistrationForm(forms.ModelForm):    
    class Meta:
        model = AdminSKPD
        fields = ['nama']