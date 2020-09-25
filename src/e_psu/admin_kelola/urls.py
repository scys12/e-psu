from django.urls import path

from . import views

app_name = "admin_kelola"
urlpatterns = [
    path("login", views.login_admin_kelola, name="login"),
    path("register", views.register_admin_kelola, name="register"),
    path("logout", views.logout_admin_kelola, name="logout"),
    path("dashboard", views.index, name="index"),
    path("serah_terima/tambah", views.serah_terima_tambah, name="serah_terima_tambah"),
    path("serah_terima/tampil/<int:id>", views.serah_terima_tampil, name="serah_terima_tampil"),
    path("serah_terima/ubah/<int:id>", views.serah_terima_ubah, name="serah_terima_ubah"),
    path("serah_terima/hapus/<int:id>", views.serah_terima_hapus, name="serah_terima_hapus"),
]