# from django.contrib.auth.decorators import login_required
# from account.decorators import admin_kelola_required
# from django.contrib import messages
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpResponse, Http404
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import DokumenForm
# from .models import Dokumen
# from admin_kelola.models import AdminKelola

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def index(request):    
#     dokumen_list = Dokumen.objects.select_related()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(dokumen_list, 10)
#     try:
#         dokumens = paginator.page(page)
#     except PageNotAnInteger:
#         dokumens = paginator.page(1)
#     except EmptyPage:
#         dokumens = paginator.page(paginator.num_pages)

#     return render(request, "serah_terima/index.html", {
#         'dokumens' : dokumens
#     })

# @login_required
# @admin_kelola_required
# def cari(request):
#     dokumen_list = Dokumen.objects.filter(nama_psu__icontains=request.GET['psu'])
#     page = request.GET.get('page', 1)

#     paginator = Paginator(dokumen_list, 10)
#     try:
#         dokumens = paginator.page(page)
#     except PageNotAnInteger:
#         dokumens = paginator.page(1)
#     except EmptyPage:
#         dokumens = paginator.page(paginator.num_pages)

#     return render(request, "serah_terima/cari.html", {
#         'dokumens' : dokumens
#     })

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def tambah(request):    
#     if request.method == 'POST':
#         form = DokumenForm(request.POST, request.FILES)
#         if form.is_valid():
#             admin = AdminKelola.objects.get(pk=request.user.id)
#             form_serah_terima = form.save(commit=False)
#             form_serah_terima.admin_kelola = admin
#             form_serah_terima.save()
#             nama_psu = form.cleaned_data.get('nama_psu')
#             messages.success(request, f'Dokumen berhasil ditambahkan.', extra_tags='serah_terima')
#             return redirect('admin_kelola:index')
#     else:
#         form = DokumenForm()
#     return render(request, "serah_terima/tambah.html", {
#         'form' : form
#     })

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def tampil(request, id):
#     dokumen = Dokumen.objects.get(id=id)
#     return render(request, "serah_terima/tampil.html", {
#         'dokumen' : dokumen
#     })

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def ubah(request, id):
#     try:
#         dokumen = Dokumen.objects.get(id = id)
#     except Dokumen.DoesNotExist:
#         return redirect('admin_kelola:index')
    
#     form = DokumenForm(request.POST or None, request.FILES or None, instance = dokumen)

#     if form.is_valid():
#         admin = AdminKelola.objects.get(pk=request.user.id)
#         form_serah_terima = form.save(commit=False)
#         form_serah_terima.admin_kelola = admin
#         form_serah_terima.save()
#         messages.success(request, f'Dokumen berhasil diperbarui.', extra_tags='serah_terima')
#         return redirect('admin_kelola:index')

#     print(form.errors)
#     return render(request, "serah_terima/ubah.html", {
#         'form' : form, 'dokumen' : dokumen
#     })

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def hapus(request, id):
#     try:
#         dokumen = Dokumen.objects.get(id=id)
#     except Dokumen.DoesNotExist:
#         return redirect('admin_kelola:index')

#     dokumen.delete()
#     messages.success(request, f'Dokumen berhasil dihapus.', extra_tags='serah_terima')
#     return redirect('admin_kelola:index')