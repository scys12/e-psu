from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def warga_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/warga/login'):
    # decorator for warga    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 4,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def admin_kelola_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/admin_kelola/login'):
    # decorator for admin_kelola
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 1,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def admin_skpd_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/admin_skpd/login'):
    # decorator for admin_skpd
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 3,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def perwakilan_penghuni_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/perwakilan_penghunilogin'):
    # decorator for perwakilan_penghuni
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 2,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator