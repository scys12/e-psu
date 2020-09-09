from django.urls import path

from . import views

app_name = "admin_skpd"
urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
]