# from django.contrib import messages
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpResponse, Http404
# from django.shortcuts import render, redirect, get_object_or_404
# from account.decorators import admin_kelola_required
# from django.contrib.auth.decorators import login_required
# from .forms import BerkasLaporanForm
# from .models import BerkasLaporan
# from admin_skpd.models import AdminSKPD

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def laporan_tambah(request):
#     if request.method == 'POST':
#         form = BerkasLaporanForm(request.POST, request.FILES)
#         if form.is_valid():
#             form_laporan = form.save(commit=False)
#             form_laporan.status_laporan = 'BELUM'
#             form_laporan.user_created = request.user
#             form_laporan.save()
#             nama_psu_laporan = form.cleaned_data.get('nama_psu_laporan')
#             messages.success(request, f'Laporan {nama_psu_laporan} berhasil ditambahkan.', extra_tags='laporan')
#             return redirect('admin_kelola:index')
#     else:
#         form = BerkasLaporanForm()

#     return render(request, "admin_kelola/laporan/tambah.html", {
#         'form': form
#     })

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def laporan_tampil(request, id):
#     laporan = BerkasLaporan.objects.get(id=id)
#     return render(request, "admin_kelola/laporan/tampil.html", {
#         'laporan': laporan
#     })
    

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def laporan_ubah(request, id):
#     try:
#         laporan = BerkasLaporan.objects.get(id=id)
#     except BerkasLaporan.DoesNotExist:
#         return redirect('admin_kelola:index')
    
#     form = BerkasLaporanForm(request.POST or None, request.FILES or None, instance = laporan)

#     if form.is_valid():
#         form.save()
#         nama_psu = form.cleaned_data.get('nama_psu_laporan')
#         messages.success(request, f'Laporan {nama_psu} berhasil diperbarui.', extra_tags='laporan')
#         return redirect('admin_kelola:index')

#     return render(request, 'admin_kelola/laporan/ubah.html', {
#         'form': form
#     })

# @login_required(login_url='/admin_kelola/login')
# @admin_kelola_required
# def laporan_hapus(request, id):
#     try:
#         laporan = BerkasLaporan.objects.get(id=id)
#     except BerkasLaporan.DoesNotExist:
#         return redirect('admin_kelola:index')
#     laporan.delete()
#     messages.success(request, f'Laporan {laporan.nama_psu_laporan} berhasil dihapus.', extra_tags='laporan')
#     return redirect('admin_kelola:index')
