from django.urls import path

from . import views

app_name = "admin_skpd"
urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path('dashboard', views.index, name="index"),
    path('logout', views.logout_admin_skpd, name="logout")
]