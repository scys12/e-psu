from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import AdminKelolaRegistrationForm
from perwakilan_penghuni.forms import PerwakilanPenghuniForm
from account.forms import RegisterForm, LoginForm, EditAccountForm
from django.db import transaction
from perwakilan_penghuni.models import PerwakilanPenghuni
from serah_terima.models import Dokumen
from laporan.models import BerkasLaporan
from serah_terima.forms import DokumenForm
from laporan.forms import BerkasLaporanForm, PersetujuanLaporan
from account.decorators import admin_kelola_required, anonymous_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from e_psu.helpers import paginate_object
from .models import AdminKelola
# Create your views here.
dokumen_list = Dokumen.objects.select_related()
laporan_reject_list = BerkasLaporan.objects.filter(is_approve=False)
laporan_accepted_list = BerkasLaporan.objects.filter(is_approve=True)
perwakilan_penghuni_list = PerwakilanPenghuni.objects.all()  
laporan_null_approve_list = BerkasLaporan.objects.filter(is_approve=None)

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def index(request):    
    page = request.GET.get('page', 1)

    page_dokumens = paginate_object(dokumen_list, 10, page)

    page_laporans_reject = paginate_object(laporan_reject_list, 10, page)

    page_laporans_accepted = paginate_object(laporan_accepted_list, 10, page)

    page_perwakilan_penghunis = paginate_object(perwakilan_penghuni_list, 10, page)

    page_laporans_null_approve = paginate_object(laporan_null_approve_list, 10, page)
    
    return render(request, "admin_kelola/index.html", {
        'dokumens' : page_dokumens,
        'laporans_reject': page_laporans_reject,
        'laporans_accepted': page_laporans_accepted,
        'perwakilan_penghunis': page_perwakilan_penghunis,
        'laporans_null_approve': page_laporans_null_approve
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
    perwakilan_penghuni = PerwakilanPenghuniForm(request.POST or None, prefix='perwakilan_penghuni')
    context = {
        "perwakilan_penghuni_form" : perwakilan_penghuni
    }

    if request.method == 'POST':
        form = DokumenForm(request.POST)
        if perwakilan_penghuni.is_valid():
            if not PerwakilanPenghuni.objects.filter(warga=request.POST['perwakilan_penghuni-warga'], data_proyek=request.POST['perwakilan_penghuni-data_proyek']):
                perwakilan_penghuni.save()
            messages.success(request, f'Perwakilan penghuni berhasil ditambahkan.', extra_tags='perwakilan_penghuni')
            return redirect('admin_kelola:index')

    return render(request, 'admin_kelola/perwakilan_penghuni/tambah.html', context)

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def perwakilan_penghuni_hapus(request, id):
    try:
        perwakilan_penghuni = PerwakilanPenghuni.objects.get(id=id)
    except PerwakilanPenghuni.DoesNotExist:
        return redirect('admin_kelola:index')

    perwakilan_penghuni.delete()
    messages.success(request, f'Dokumen berhasil dihapus.', extra_tags='perwakilan_penghuni')
    return redirect('admin_kelola:index')

# SERAH TERIMA
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
    try:
        dokumen = Dokumen.objects.get(id=id)
    except dokumen.DoesNotExist:
        return redirect('admin_kelola:index')    
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

# LAPORAN
@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def laporan_tambah(request):
    if request.method == 'POST':
        form = BerkasLaporanForm(request.POST, request.FILES)
        if form.is_valid():
            form_laporan = form.save(commit=False)
            form_laporan.status_laporan = 'BELUM'
            form_laporan.is_approve = True
            form_laporan.user_created = request.user
            form_laporan.save()
            nama_psu_laporan = form.cleaned_data.get('nama_psu_laporan')
            messages.success(request, f'Laporan {nama_psu_laporan} berhasil ditambahkan.', extra_tags='laporan')
            return redirect('admin_kelola:index')
    else:
        form = BerkasLaporanForm()

    return render(request, "admin_kelola/laporan/tambah.html", {
        'form': form
    })

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def laporan_tampil(request, id):
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('admin_kelola:index')
    return render(request, "admin_kelola/laporan/tampil.html", {
        'laporan': laporan
    })
    

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def laporan_ubah(request, id):
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('admin_kelola:index')
    
    form = BerkasLaporanForm(request.POST or None, request.FILES or None, instance = laporan)

    if form.is_valid():
        form.save()
        nama_psu = form.cleaned_data.get('nama_psu_laporan')
        messages.success(request, f'Laporan {nama_psu} berhasil diperbarui.', extra_tags='laporan')
        return redirect('admin_kelola:index')

    return render(request, 'admin_kelola/laporan/ubah.html', {
        'form': form
    })

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def laporan_hapus(request, id):
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('admin_kelola:index')
    laporan.delete()
    messages.success(request, f'Laporan {laporan.nama_psu_laporan} berhasil dihapus.', extra_tags='laporan')
    return redirect('admin_kelola:index')

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def detail_form_persetujuan_view(request, id):
    query_laporan = laporan_null_approve_list.filter(id=id)
    if query_laporan.count() < 1:
        return redirect('admin_kelola:index')
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('admin_kelola:index')
    persetujuan_laporan_form = PersetujuanLaporan(request.POST or None, instance=laporan)
    if persetujuan_laporan_form.is_valid():
        persetujuan_laporan_form.save()
        nama_psu = laporan.nama_psu_laporan
        messages.success(request, f'Laporan {nama_psu} berhasil diperbarui.', extra_tags='laporan')
        return redirect('admin_kelola:index')
    return render(request, "admin_kelola/laporan/detail_persetujuan.html", {
        'laporan': laporan,
        'persetujuan_laporan_form' : persetujuan_laporan_form
    })

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def change_profile_view(request):
    admin_kelola = AdminKelola.objects.get(user_id=request.user.id)
    admin_kelola_form = AdminKelolaRegistrationForm(request.POST or None, prefix='admin_kelola',instance = admin_kelola)
    account = EditAccountForm(request.POST or None, prefix='account', instance= request.user)
    if admin_kelola_form.is_valid() and account.is_valid():
        admin_kelola_form.save()
        account.save()
        messages.success(request, f'Profile berhasil diperbarui.')
        return redirect('admin_kelola:display_profile')
    context = {
        "admin_kelola_form" : admin_kelola_form,
        "account" : account,
    }
    return render(request, 'admin_kelola/auth/change_profile.html', context)

@login_required(login_url='/admin_kelola/login')
@admin_kelola_required
def display_profile_view(request):
    admin_kelola = AdminKelola.objects.get(user_id=request.user.id)
    context = {
        "admin_kelola" : admin_kelola
    }
    return render(request, 'admin_kelola/auth/display_profile.html', context)