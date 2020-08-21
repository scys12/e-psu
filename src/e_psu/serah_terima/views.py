from django.shortcuts import render, redirect

from .forms import DokumenForm
from .models import Dokumen

def index(request):
    dokumens = Dokumen.objects.all()
    return render(request, "serah_terima/index.html", {
        'dokumens' : dokumens
    })

def tambah(request):
    if request.method == 'POST':
        form = DokumenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('serah_terima:index')
    else:
        form = DokumenForm()

    return render(request, "serah_terima/upload_form.html", {
        'form' : form
    })

def tampil(request, id):
    dokumen = Dokumen.objects.get(id=id);
    return render(request, "serah_terima/tampil.html", {
        'dokumen' : dokumen
    })

def ubah(request, id):
    try:
        dokumen = Dokumen.objects.get(id = id)
    except Dokumen.DoesNotExist:
        return redirect('serah_terima:index')
    
    form = DokumenForm(request.POST or None, request.FILES or None, instance = dokumen)

    if form.is_valid():
       form.save()
       return redirect('serah_terima:index')

    return render(request, "serah_terima/upload_form.html", {
        'form' : form
    })

def hapus(request, id):
    try:
        dokumen = Dokumen.objects.get(id = id)
    except Dokumen.DoesNotExist:
        return redirect('serah_terima:index')

    dokumen.delete()
    return redirect('serah_terima:index')