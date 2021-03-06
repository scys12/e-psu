from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WargaRegistrationForm
from account.forms import RegisterForm, LoginForm, EditAccountForm
from account.decorators import anonymous_required, warga_required
from django.db import transaction
from django.contrib.auth.decorators import login_required
from laporan.models import BerkasLaporan
from django.contrib.auth import logout
from laporan.forms import BerkasLaporanForm
from e_psu.helpers import paginate_object
from .models import Warga
from serah_terima.models import Dokumen
from perwakilan_penghuni.models import PerwakilanPenghuni
# Create your views here.
@login_required(login_url='/warga/login')
@warga_required
def index_view(request):
    page = request.GET.get('page', 1)
    semua_laporan = BerkasLaporan.objects.filter(user_created_id=request.user.id)
    laporans = paginate_object(semua_laporan, 10, page)

    all_laporan = BerkasLaporan.objects.exclude(user_created_id=request.user.id)
    all_laporan_masyarakat = paginate_object(all_laporan, 10, page)

    warga = Warga.objects.get(user_id=request.user.id)
    data_proyek_ids = set(PerwakilanPenghuni.objects.filter(warga_id=warga.id).values_list('data_proyek', flat=True).distinct())
    
    semua_data_serah_terima = Dokumen.objects.filter(data_proyek_id__in=[id for id in data_proyek_ids])
    all_dokumen_serah_terima = paginate_object(semua_data_serah_terima, 10, page)

    return render(request, "warga/index.html", {
        'laporans': laporans,
        'all_laporan_masyarakat': all_laporan_masyarakat,
        'dokumens' : all_dokumen_serah_terima
    })

@login_required(login_url='/warga/login')
@warga_required
def serah_terima_tampil(request, id):
    try:
        dokumen = Dokumen.objects.get(id=id)
    except Dokumen.DoesNotExist:
        return redirect('warga:index')    
    return render(request, "warga/serah_terima/tampil.html", {
        'dokumen' : dokumen
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
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('warga:index')
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
    warga = Warga.objects.get(user_id=request.user.id)
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
    warga = Warga.objects.get(user_id=request.user.id)
    context = {
        "warga" : warga
    }
    return render(request, 'warga/auth/display_profile.html', context)