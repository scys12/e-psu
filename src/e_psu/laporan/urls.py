from django.urls import path

from . import views

app_name = "laporan"
urlpatterns = [
    path("admin_kelola/tambah", views.tambah, name="tambah"),
    path("tampil/<int:id>", views.tampil, name="tampil"),
    path("ubah/<int:id>", views.ubah, name="ubah"),
    path("hapus/<int:id>", views.hapus, name="hapus"),
]