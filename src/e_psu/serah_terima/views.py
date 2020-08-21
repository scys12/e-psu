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

    return render(request, "serah_terima/tambah.html", {
        'form' : form
    })

def tampil(request):
    form = DokumenForm()
    return render(request, "serah_terima/tampil.html", {
        'form' : form
    })