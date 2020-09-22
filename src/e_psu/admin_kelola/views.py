from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import AdminKelolaRegistrationForm
from account.forms import RegisterForm, LoginForm
from django.db import transaction
from serah_terima.models import Dokumen
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account.decorators import admin_kelola_required, anonymous_required
from django.contrib.auth.decorators import login_required
from laporan.models import BerkasLaporan
# Create your views here.

def login(request):
    return render(request, "admin_kelola/auth/login.html")

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def index(request):    
    page = request.GET.get('page', 1)

    dokumen_list = Dokumen.objects.select_related()
    paginator = Paginator(dokumen_list, 10)
    try:
        dokumens = paginator.page(page)
    except PageNotAnInteger:
        dokumens = paginator.page(1)
    except EmptyPage:
        dokumens = paginator.page(paginator.num_pages)
    
    semua_laporan = BerkasLaporan.objects.all()  
    paginator_laporan = Paginator(semua_laporan, 10)
    try:
        laporans = paginator_laporan.page(page)
    except PageNotAnInteger:
        laporans = paginator_laporan.page(1)
    except EmptyPage:
        laporans = paginator_laporan.page(paginator_laporan.num_pages)

    return render(request, "admin_kelola/index.html", {
        'dokumens' : dokumens,
        'laporans': laporans
    })    

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

@anonymous_required
def login_admin_kelola(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='admin')
    context = {
        "form" : account
    }
    if account.is_valid():
        return redirect('admin_kelola:index')
    return render(request, 'admin_kelola/auth/login.html', context)

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def logout_admin_kelola(request):
    logout(request)
    return redirect('home')