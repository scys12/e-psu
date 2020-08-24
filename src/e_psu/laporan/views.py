from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BerkasLaporanForm
from .models import BerkasLaporan

def index(request):
    semua_laporan = BerkasLaporan.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(semua_laporan, 10)
    try:
        laporans = paginator.page(page)
    except PageNotAnInteger:
        laporans = paginator.page(1)
    except EmptyPage:
        laporans = paginator.page(paginator.num_pages)

    return render(request, "laporan/index.html", {
        'laporans': laporans
    })

def tambah(request):
    if request.method == 'POST':
        form = BerkasLaporanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nama_psu = form.cleaned_data.get('nama_psu')
            messages.success(request, f'Laporan {nama_psu} berhasil ditambahkan.')
            return redirect('laporan:index')
    else:
        form = BerkasLaporanForm()

    return render(request, "laporan/tambah.html", {
        'form': form
    })

def tampil(request, id):
    laporan = BerkasLaporan.objects.get(id=id)
    return render(request, "laporan/tampil.html", {
        'laporan': laporan
    })

def ubah(request, id):
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('laporan:index')
    
    form = BerkasLaporanForm(request.POST or None, request.FILES or None, instance = laporan)

    if form.is_valid():
        form.save()
        nama_psu = form.cleaned_data.get('nama_psu')
        messages.success(request, f'Laporan {nama_psu} berhasil diperbarui.')
        return redirect('laporan:tampil', id=id)

    return render(request, 'laporan/ubah.html', {
        'form': form
    })

def hapus(request, id):
    try:
        laporan = BerkasLaporan.objects.get(id=id)
    except BerkasLaporan.DoesNotExist:
        return redirect('laporan:index')

    laporan.delete()
    messages.success(request, f'Laporan {laporan.nama_psu} berhasil dihapus.')
    return redirect('laporan:index')
