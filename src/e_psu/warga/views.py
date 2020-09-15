from django.shortcuts import render, redirect, get_object_or_404
from .forms import WargaRegistrationForm
from account.forms import RegisterForm, LoginForm
from django.db import transaction
# Create your views here.


def login(request):
    return render(request, "warga/auth/login.html")


@transaction.atomic
def register(request):
    account = RegisterForm(request.POST or None, prefix='account')
    warga = WargaRegistrationForm(request.POST or None, prefix='warga')
    context = {
        "warga_form" : warga,
        "account_form" : account
    }
    if account.is_valid() and warga.is_valid():
        user = account.save(commit=False)
        user.user_type = 4
        user.save()
        warga_data = warga.save(commit=False)
        warga_data.user = user
        warga_data.save()
        return redirect('warga:login')
    return render(request, 'warga/auth/register.html', context)

def login(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='warga')
    context = {
        "form" : account
    }
    if account.is_valid():
        return render(request, 'warga/auth/register.html',context)
    return render(request, 'warga/auth/login.html', context)