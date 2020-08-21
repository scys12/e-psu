from django.urls import path

from . import views

app_name = "serah_terima"
urlpatterns = [
    path("", views.index, name="index"),
    path("tambah", views.tambah, name="tambah"),
    path("tampil", views.tampil, name="tampil"),
]