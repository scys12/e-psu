from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BerkasLaporanForm
from .models import BerkasLaporan

def index(request):
    semua_laporan = BerkasLaporan.objects.all()
    return render(request, "laporan/index.html", {
        'semua_laporan': semua_laporan
    })

def tambah(request):
    if request.method == 'POST':
        form = BerkasLaporanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nama_psu = form.cleaned_data.get('nama_psu')
            message.success(request, f'Laporan {nama_psu} berhasil ditambahkan.')
            return redirect('laporan:index')
        else:
            form = BerkasLaporanForm()

    return render(request, "laporan/tambah.html", {
        'form': form
    })

# def tampil(request, id):
#     return render()

# def ubah(request, id):
#     return render()

# def hapus(request, id):
#     return redirect()
