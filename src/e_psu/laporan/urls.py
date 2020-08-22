from django.urls import path

from . import views

app_name = "laporan"
urlpatterns = [
    path("", views.index, name="index"),
    path("tambah", views.tambah, name="tambah"),
]