from django.urls import path

from . import views

app_name = "admin_kelola"
urlpatterns = [
    path("login", views.login_admin_kelola, name="login"),
    path("register", views.register_admin_kelola, name="register"),
    path("logout", views.logout_admin_kelola, name="logout"),
    path("profile", views.display_profile_view, name="display_profile"),
    path("profile/edit", views.change_profile_view, name="change_profile"),
    path("dashboard", views.index, name="index"),
    path("perwakilan_penghuni/tambah", views.perwakilan_penghuni_tambah, name="perwakilan_penghuni_tambah"),
    path("perwakilan_penghuni/hapus/<int:id>", views.perwakilan_penghuni_hapus, name="perwakilan_penghuni_hapus"),
    path("laporan/tambah", views.laporan_tambah, name="laporan_tambah"),
    path("laporan/persetujuan/<int:id>", views.detail_form_persetujuan_view, name="laporan_persetujuan"),
    path("laporan/tampil/<int:id>", views.laporan_tampil, name="laporan_tampil"),
    path("laporan/ubah/<int:id>", views.laporan_ubah, name="laporan_ubah"),
    path("laporan/hapus/<int:id>", views.laporan_hapus, name="laporan_hapus"),
    path("serah_terima/tambah", views.serah_terima_tambah, name="serah_terima_tambah"),
    path("serah_terima/tampil/<int:id>", views.serah_terima_tampil, name="serah_terima_tampil"),
    path("serah_terima/ubah/<int:id>", views.serah_terima_ubah, name="serah_terima_ubah"),
    path("serah_terima/hapus/<int:id>", views.serah_terima_hapus, name="serah_terima_hapus"),
]