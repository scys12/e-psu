from django import forms
from .models import Account
from django.core.validators import MinLengthValidator

class AccountForm(forms.ModelForm):
    password = forms.CharField(validators=[MinLengthValidator(4, "Password terlalu pendek")], widget=forms.PasswordInput(attrs={'class' : 'fadeIn second'}))
    konfirmasi_password = forms.CharField(validators=[MinLengthValidator(4, "Konfirmasi Password terlalu pendek")], widget=forms.PasswordInput(attrs={'class' : 'fadeIn second'})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'fadeIn second'}))
    username = forms.CharField(validators=[MinLengthValidator(4, "Username terlalu pendek")],widget=forms.TextInput(attrs={'class' : 'fadeIn second'}))

    class Meta:
        model = Account
        fields = ['email', 'username', 'password']