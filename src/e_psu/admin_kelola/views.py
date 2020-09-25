from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import AdminKelolaRegistrationForm
from serah_terima.forms import DokumenForm
from perwakilan_penghuni.forms import PerwakilanPenghuniForm
from account.forms import RegisterForm, LoginForm
from django.db import transaction
from perwakilan_penghuni.models import PerwakilanPenghuni
from serah_terima.models import Dokumen
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from account.decorators import admin_kelola_required, anonymous_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from laporan.models import BerkasLaporan
# Create your views here.

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

    semua_perwakilan_penghuni = PerwakilanPenghuni.objects.all()  
    paginator_penghuni = Paginator(semua_perwakilan_penghuni, 10)
    try:
        perwakilan_penghunis = paginator_penghuni.page(page)
    except PageNotAnInteger:
        perwakilan_penghunis = paginator_penghuni.page(1)
    except EmptyPage:
        perwakilan_penghunis = paginator_penghuni.page(paginator_penghuni.num_pages)

    return render(request, "admin_kelola/index.html", {
        'dokumens' : dokumens,
        'laporans': laporans,
        'perwakilan_penghunis': perwakilan_penghunis
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

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def perwakilan_penghuni_tambah(request):    
    account = RegisterForm(request.POST or None, prefix='account')
    perwakilan_penghuni = PerwakilanPenghuniForm(request.POST or None, prefix='perwakilan_penghuni')
    context = {
        "perwakilan_penghuni_form" : perwakilan_penghuni,
        "account_form" : account
    }
    if account.is_valid() and perwakilan_penghuni.is_valid():
        user = account.save(commit=False)
        user.user_type = 2
        user.save()
        perwakilan_penghuni_data = perwakilan_penghuni.save(commit=False)
        perwakilan_penghuni_data.user = user
        perwakilan_penghuni_data.save()
        return redirect('admin_kelola:index')
    return render(request, 'admin_kelola/perwakilan_penghuni/tambah.html', context)


@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def serah_terima_tambah(request):    
    if request.method == 'POST':
        form = DokumenForm(request.POST, request.FILES)
        if form.is_valid():
            admin = AdminKelola.objects.get(pk=request.user.id)
            form_serah_terima = form.save(commit=False)
            form_serah_terima.admin_kelola = admin
            form_serah_terima.save()
            nama_psu = form.cleaned_data.get('nama_psu')
            messages.success(request, f'Dokumen berhasil ditambahkan.', extra_tags='serah_terima')
            return redirect('admin_kelola:index')
    else:
        form = DokumenForm()
    return render(request, "admin_kelola/serah_terima/tambah.html", {
        'form' : form
    })

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def serah_terima_tampil(request, id):
    dokumen = Dokumen.objects.get(id=id)
    return render(request, "admin_kelola/serah_terima/tampil.html", {
        'dokumen' : dokumen
    })

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def serah_terima_ubah(request, id):
    try:
        dokumen = Dokumen.objects.get(id = id)
    except Dokumen.DoesNotExist:
        return redirect('admin_kelola:index')
    
    form = DokumenForm(request.POST or None, request.FILES or None, instance = dokumen)

    if form.is_valid():
        admin = AdminKelola.objects.get(pk=request.user.id)
        form_serah_terima = form.save(commit=False)
        form_serah_terima.admin_kelola = admin
        form_serah_terima.save()
        messages.success(request, f'Dokumen berhasil diperbarui.', extra_tags='serah_terima')
        return redirect('admin_kelola:index')

    print(form.errors)
    return render(request, "admin_kelola/serah_terima/ubah.html", {
        'form' : form, 'dokumen' : dokumen
    })

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def serah_terima_hapus(request, id):
    try:
        dokumen = Dokumen.objects.get(id=id)
    except Dokumen.DoesNotExist:
        return redirect('admin_kelola:index')

    dokumen.delete()
    messages.success(request, f'Dokumen berhasil dihapus.', extra_tags='serah_terima')
    return redirect('admin_kelola:index')
