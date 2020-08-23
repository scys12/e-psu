from django import forms
from .models import Masyarakat
from django.core.validators import MinLengthValidator
class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(validators=[MinLengthValidator(4, "Password terlalu pendek")], widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(validators=[MinLengthValidator(4, "Konfirmasi Password terlalu pendek")], widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'Confirmation Password'}))
    name = forms.CharField(validators=[MinLengthValidator(4, "Nama terlalu pendek")], widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(validators=[MinLengthValidator(4, "Username terlalu pendek")],widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = Masyarakat
        fields = ['name','username','password','email']

    def clean_password(self):
        user_data = self.cleaned_data
        print(user_data)
        if user_data['password'] != user_data['confirm_password']:
            return forms.ValidationError("Password tidak sama")

        return user_data['password']