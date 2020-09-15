from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import AdminKelolaRegistrationForm
from account.forms import RegisterForm, LoginForm
from django.db import transaction
# Create your views here.


def login(request):
    return render(request, "admin_kelola/auth/login.html")


@transaction.atomic
def register_admin_kelola(request):
    account = RegisterForm(request.POST or None, prefix='account')
    admin_kelola = AdminKelolaRegistrationForm(request.POST or None, prefix='admin_kelola')
    context = {
        "admin_kelola_form" : admin_kelola,
        "account_form" : account
    }
    if account.is_valid() and admin_kelola.is_valid():
        user = account.save(commit=False)
        user.user_type = 1
        user.save()
        admin_kelola_data = admin_kelola.save(commit=False)
        admin_kelola_data.user = user
        admin_kelola_data.save()
        return redirect('admin_kelola:login')
    return render(request, 'admin_kelola/auth/register.html', context)

def login_admin_kelola(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='admin')
    context = {
        "form" : account
    }
    if account.is_valid():
        return redirect('serah_terima:index')
    return render(request, 'admin_kelola/auth/login.html', context)


def logout_admin_kelola(request):
    logout(request)
    return redirect('home')