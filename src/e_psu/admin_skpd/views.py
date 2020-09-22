from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdminSKPDRegistrationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account.forms import RegisterForm, LoginForm
from account.decorators import admin_skpd_required, anonymous_required
from django.db import transaction
from laporan.models import BerkasLaporan

# Create your views here.

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def index(request):    
    page = request.GET.get('page', 1)

    semua_laporan = BerkasLaporan.objects.all()  
    paginator_laporan = Paginator(semua_laporan, 10)
    try:
        laporans = paginator_laporan.page(page)
    except PageNotAnInteger:
        laporans = paginator_laporan.page(1)
    except EmptyPage:
        laporans = paginator_laporan.page(paginator_laporan.num_pages)

    return render(request, "admin_skpd/index.html", {
        'laporans': laporans,
    })  

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

@anonymous_required
def login(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='skpd')
    context = {
        "form" : account
    }
    if account.is_valid():
        return redirect('admin_skpd:index')
    return render(request, 'admin_skpd/auth/login.html', context)

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def logout_admin_skpd(request):
    logout(request)
    return redirect('home')