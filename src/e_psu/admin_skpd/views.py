from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdminSKPDRegistrationForm
from account.forms import RegisterForm, LoginForm
from django.db import transaction
# Create your views here.


def login(request):
    return render(request, "admin_skpd/auth/login.html")


@transaction.atomic
def register(request):
    account = RegisterForm(request.POST or None, prefix='account')
    admin_skpd = AdminSKPDRegistrationForm(request.POST or None, prefix='admin_skpd')
    context = {
        "admin_skpd_form" : admin_skpd,
        "account_form" : account
    }
    if account.is_valid() and admin_skpd.is_valid():
        user = account.save(commit=False)
        user.user_type = 3
        user.save()
        admin_skpd_data = admin_skpd.save(commit=False)
        admin_skpd_data.user = user
        admin_skpd_data.save()
        return redirect('admin_skpd:login')
    return render(request, 'admin_skpd/auth/register.html', context)

def login(request):
    account = LoginForm(data=request.POST or None, request=request)
    context = {
        "form" : account
    }
    if account.is_valid():
        print("1")
        return redirect('serah_terima:index')
    return render(request, 'admin_skpd/auth/login.html', context)