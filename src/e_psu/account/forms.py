from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.core.validators import MinLengthValidator

Account = get_user_model()

class RegisterForm(forms.ModelForm):
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
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class' : 'fadeIn second'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'fadeIn second'}))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("Email atau Password salah")
        login(request, user)
        self.user = user
        return data