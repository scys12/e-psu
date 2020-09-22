from django.shortcuts import render, redirect, get_object_or_404
from .forms import WargaRegistrationForm
from account.forms import RegisterForm, LoginForm
from account.decorators import anonymous_required, warga_required
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from laporan.models import BerkasLaporan
from django.contrib.auth import logout
# Create your views here.
@login_required(login_url='/warga/login')
@warga_required
def index(request):
    page = request.GET.get('page', 1)
    semua_laporan = BerkasLaporan.objects.all()  
    paginator_laporan = Paginator(semua_laporan, 10)
    try:
        laporans = paginator_laporan.page(page)
    except PageNotAnInteger:
        laporans = paginator_laporan.page(1)
    except EmptyPage:
        laporans = paginator_laporan.page(paginator_laporan.num_pages)

    return render(request, "warga/index.html", {
        'laporans': laporans
    })

@login_required(login_url='/warga/login')
@warga_required
def logout_warga(request):
    logout(request)
    return redirect('home')
@transaction.atomic
def register(request):
    account = RegisterForm(request.POST or None, prefix='account')
    warga = WargaRegistrationForm(request.POST or None, prefix='warga')
    context = {
        "warga_form" : warga,
        "account_form" : account
    }
    if account.is_valid() and warga.is_valid():
        user = account.save(commit=False)
        user.user_type = 4
        user.save()
        warga_data = warga.save(commit=False)
        warga_data.user = user
        warga_data.save()
        return redirect('warga:login')
    return render(request, 'warga/auth/register.html', context)

@anonymous_required
def login(request):
    account = LoginForm(data=request.POST or None, request=request, prefix='warga')
    context = {
        "form" : account
    }
    if account.is_valid():
        return redirect('warga:index')
    return render(request, 'warga/auth/login.html', context)