from django.urls import path

from . import views

app_name = "masyarakat"
urlpatterns = [
    path("signin", views.masyarakat_create_view, name="register")
]