from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WargaRegistrationForm
from account.forms import RegisterForm, LoginForm, EditAccountForm
from account.decorators import anonymous_required, warga_required
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from laporan.models import BerkasLaporan
from django.contrib.auth import logout
from laporan.forms import BerkasLaporanForm
from .models import Warga
# Create your views here.
@login_required(login_url='/warga/login')
@warga_required
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

    return render(request, "warga/index.html", {
        'laporans': laporans
    })

@login_required(login_url='/warga/login')
@warga_required
def logout_view(request):
    logout(request)
    return redirect('home')

@transaction.atomic
def register_view(request):
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

@anonymous_required
def login_view(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='warga')
    context = {
        "form" : account
    }
    if account.is_valid():
        return redirect('warga:index')
    return render(request, 'warga/auth/login.html', context)

@login_required(login_url='/warga/login')
@warga_required
def detail_laporan_view(request, id):
    laporan = BerkasLaporan.objects.get(id=id)
    return render(request, "warga/laporan/detail_laporan.html", {
        'laporan': laporan
    })

@login_required(login_url='/warga/login')
@warga_required
def add_laporan_view(request):
    form = BerkasLaporanForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form_laporan = form.save(commit=False)
        form_laporan.status_laporan = 'BELUM'
        form_laporan.user_created = request.user
        form_laporan.save()
        nama_psu_laporan = form.cleaned_data.get('nama_psu_laporan')
        messages.success(request, f'Laporan {nama_psu_laporan} berhasil ditambahkan.', extra_tags='laporan')
        return redirect('warga:index')
    return render(request, "warga/laporan/add_laporan.html", {
        'form': form
    })

@login_required(login_url='/warga/login')
@warga_required
def change_profile_view(request):
    warga = Warga.objects.get(pk=request.user.id)
    warga_form = WargaRegistrationForm(request.POST or None, prefix='warga',instance = warga)
    account = EditAccountForm(request.POST or None, prefix='account', instance= request.user)
    if warga_form.is_valid() and account.is_valid():
        warga_form.save()
        account.save()
        messages.success(request, f'Profile berhasil diperbarui.')
        return redirect('warga:display_profile')
    context = {
        "warga_form" : warga_form,
        "account" : account,
    }
    return render(request, 'warga/auth/change_profile.html', context)

@login_required(login_url='/warga/login')
@warga_required
def display_profile_view(request):
    warga = Warga.objects.get(pk=request.user.id)
    context = {
        "warga" : warga
    }
    return render(request, 'warga/auth/display_profile.html', context)