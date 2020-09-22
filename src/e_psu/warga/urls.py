from django.urls import path

from . import views

app_name = "warga"
urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout_warga, name="logout"),
    path("register", views.register, name="register"),
    path("dashboard", views.index, name="index"),
]