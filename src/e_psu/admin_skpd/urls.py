from django.urls import path

from . import views

app_name = "admin_skpd"
urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path('dashboard', views.index_view, name="index"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.display_profile_view, name="display_profile"),
    path('profile/edit', views.change_profile_view, name="change_profile"),
    path("laporan/<int:id>", views.detail_laporan_view, name="detail_laporan"),
    path("laporan/edit/<int:id>", views.update_laporan_view, name="update_laporan"),
]