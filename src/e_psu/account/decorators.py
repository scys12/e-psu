from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

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
        lambda u: u.is_active and (u.user_type == 1),
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

def perwakilan_penghuni_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/perwakilan_penghuni/login'):
    # decorator for perwakilan_penghuni
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.user_type == 2,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def anonymous_required( view_function, redirect_to = None ):
    return AnonymousRequired( view_function, redirect_to )

class AnonymousRequired( object ):
    def __init__( self, view_function, redirect_to ):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGIN_REDIRECT_URL
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__( self, request, *args, **kwargs ):
        if request.user is not None and request.user.is_authenticated:
            print(request.user)
            if request.user.user_type == 1:
                redirect_to = '/admin_kelola/dashboard'
            elif request.user.user_type == 3:
                redirect_to = '/admin_skpd/dashboard'
            elif request.user.user_type == 4:
                redirect_to = '/warga/dashboard'
            return HttpResponseRedirect( redirect_to )
        return self.view_function( request, *args, **kwargs )