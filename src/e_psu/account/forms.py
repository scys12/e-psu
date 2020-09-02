from django import forms
from .models import Account
from django.core.validators import MinLengthValidator

class AccountForm(forms.ModelForm):
    password = forms.CharField(label='Password', validators=[MinLengthValidator(4, "Password terlalu pendek")], widget=forms.PasswordInput(attrs={'class' : 'fadeIn second'}))
    konfirmasi_password = forms.CharField(label='Konfirmasi Password', validators=[MinLengthValidator(4, "Konfirmasi Password terlalu pendek")], widget=forms.PasswordInput(attrs={'class' : 'fadeIn second'})) 
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class' : 'fadeIn second'}))
    username = forms.CharField(label='Username', validators=[MinLengthValidator(4, "Username terlalu pendek")],widget=forms.TextInput(attrs={'class' : 'fadeIn second'}))

    class Meta:
        model = Account
        fields = ['email', 'username']
    
    def clean_konfirmasi_password(self):
        password = self.cleaned_data.get("password")
        konfirmasi_password = self.cleaned_data.get("konfirmasi_password")
        if password and konfirmasi_password and password != konfirmasi_password:
            raise forms.ValidationError("Password tidak sama")
        return password
    
    def save(self, commit=True):
        user = super(AccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user