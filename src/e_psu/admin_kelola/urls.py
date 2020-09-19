from django.urls import path

from . import views

app_name = "admin_kelola"
urlpatterns = [
    path("login", views.login_admin_kelola, name="login"),
    path("register", views.register_admin_kelola, name="register"),
    path("logout", views.logout_admin_kelola, name="logout"),
    path("dashboard", views.index, name="index")
]