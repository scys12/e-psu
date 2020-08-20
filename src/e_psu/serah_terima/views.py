from django.shortcuts import render

def index(request):
    return render(request, "serah_terima/index.html")

def tambah(request):
    return render(request, "serah_terima/tambah.html")