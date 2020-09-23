from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdminSKPDRegistrationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account.forms import RegisterForm, LoginForm, EditAccountForm
from account.decorators import admin_skpd_required, anonymous_required
from django.db import transaction
from laporan.models import BerkasLaporan
from laporan.forms import UpdateStatusForm, UpdatePenangananForm
from .models import AdminSKPD
# Create your views here.

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def index_view(request):    
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
def register_view(request):
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
def login_view(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='skpd')
    context = {
        "form" : account
    }
    if account.is_valid():
        return redirect('admin_skpd:index')
    return render(request, 'admin_skpd/auth/login.html', context)

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def display_profile_view(request):
    admin_skpd = AdminSKPD.objects.get(pk=request.user.id)
    context = {
        "admin_skpd" : admin_skpd
    }
    return render(request, 'admin_skpd/auth/display_profile.html', context)

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def change_profile_view(request):
    admin_skpd = AdminSKPD.objects.get(pk=request.user.id)
    account = EditAccountForm(request.POST or None, prefix='account', instance= request.user)
    admin_skpd_form = AdminSKPDRegistrationForm(request.POST or None, prefix='admin_skpd',instance = admin_skpd)
    if admin_skpd_form.is_valid() and account.is_valid():
        admin_skpd_form.save()
        account.save()
        messages.success(request, f'Profile berhasil diperbarui.')
        return redirect('admin_skpd:display_profile')
    context = {
        "admin_skpd_form" : admin_skpd_form,
        "account" : account,
    }
    return render(request, 'admin_skpd/auth/change_profile.html', context)

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def detail_laporan_view(request, id):
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('admin_skpd:index')

    return render(request, "admin_skpd/laporan/detail_laporan.html", {
        'laporan': laporan
    })

@login_required(login_url='/admin_skpd/login')
@admin_skpd_required
def update_laporan_view(request, id):
    try:
        berkas_laporan = BerkasLaporan.objects.get(id=id)
    except:
        return redirect('admin_skpd:index')

    update_status_form = UpdateStatusForm(request.POST or None, instance=berkas_laporan)
    update_penanganan_form = UpdatePenangananForm(request.POST or None, instance=berkas_laporan)

    if update_status_form.is_valid():
        admin_skpd = AdminSKPD.objects.get(pk=request.user.id)
        berkas_laporan = update_status_form.save(commit=False)
        berkas_laporan.admin_status_laporan = admin_skpd
        berkas_laporan.save()
        messages.success(request, f'Laporan {id} berhasil diperbaharui', extra_tags='laporan')
        return redirect('admin_skpd:index')    
    elif update_penanganan_form.is_valid():        
        admin_skpd = AdminSKPD.objects.get(pk=request.user.id)
        berkas_laporan = update_penanganan_form.save(commit=False)
        berkas_laporan.admin_penanganan_laporan = admin_skpd
        berkas_laporan.save()
        messages.success(request, f'Laporan {id} berhasil diperbaharui', extra_tags='laporan')
        return redirect('admin_skpd:index')

    return render(request, "admin_skpd/laporan/update_laporan.html", {
        'update_status_form': update_status_form,
        'update_penanganan_form': update_penanganan_form,
    })