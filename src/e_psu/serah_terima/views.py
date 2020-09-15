from django.contrib.auth.decorators import login_required
from account.decorators import admin_kelola_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DokumenForm
from .models import Dokumen


@login_required
@admin_kelola_required
def index(request):
    dokumen_list = Dokumen.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(dokumen_list, 10)
    try:
        dokumens = paginator.page(page)
    except PageNotAnInteger:
        dokumens = paginator.page(1)
    except EmptyPage:
        dokumens = paginator.page(paginator.num_pages)

    return render(request, "serah_terima/index.html", {
        'dokumens' : dokumens
    })

@login_required
@admin_kelola_required
def cari(request):
    dokumen_list = Dokumen.objects.filter(nama_psu__icontains=request.GET['psu'])
    page = request.GET.get('page', 1)

    paginator = Paginator(dokumen_list, 10)
    try:
        dokumens = paginator.page(page)
    except PageNotAnInteger:
        dokumens = paginator.page(1)
    except EmptyPage:
        dokumens = paginator.page(paginator.num_pages)

    return render(request, "serah_terima/cari.html", {
        'dokumens' : dokumens
    })

@login_required
@admin_kelola_required
def tambah(request):
    if request.method == 'POST':
        form = DokumenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nama_psu = form.cleaned_data.get('nama_psu')
            messages.success(request, f'Dokumen {nama_psu} berhasil ditambahkan.')
            return redirect('serah_terima:index')
    else:
        form = DokumenForm()

    return render(request, "serah_terima/tambah.html", {
        'form' : form
    })

@login_required
@admin_kelola_required
def tampil(request, id):
    dokumen = Dokumen.objects.get(id=id)
    return render(request, "serah_terima/tampil.html", {
        'dokumen' : dokumen
    })

@login_required
@admin_kelola_required
def ubah(request, id):
    try:
        dokumen = Dokumen.objects.get(id = id)
    except Dokumen.DoesNotExist:
        return redirect('serah_terima:index')
    
    form = DokumenForm(request.POST or None, request.FILES or None, instance = dokumen)

    if form.is_valid():
       form.save()
       nama_psu = form.cleaned_data.get('nama_psu')
       messages.success(request, f'Dokumen {nama_psu} berhasil diperbarui.')
       return redirect('serah_terima:tampil', id=id)

    return render(request, "serah_terima/ubah.html", {
        'form' : form
    })

@login_required
@admin_kelola_required
def hapus(request, id):
    try:
        dokumen = Dokumen.objects.get(id=id)
    except Dokumen.DoesNotExist:
        return redirect('serah_terima:index')

    dokumen.delete()
    messages.success(request, f'Dokumen {dokumen.nama_psu} berhasil dihapus.')
    return redirect('serah_terima:index')