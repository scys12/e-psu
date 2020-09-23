from django.urls import path

from . import views

app_name = "warga"
urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("dashboard", views.index_view, name="index"),
    path("laporan/<int:id>", views.detail_laporan_view, name="detail_laporan"),
    path("laporan", views.add_laporan_view, name="add_laporan"),
    path("profile", views.display_profile_view, name="display_profile"),
    path("profile/edit", views.change_profile_view, name="change_profile"),
]