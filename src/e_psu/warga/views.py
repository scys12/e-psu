from django.shortcuts import render, redirect, get_object_or_404
from .forms import WargaRegistrationForm
from account.forms import AccountForm
from django.db import transaction
# Create your views here.


def login(request):
    return render(request, "warga/login.html")


@transaction.atomic
def register(request):
    if request.method == 'POST':
        account = AccountForm(request.POST, prefix='account')
        warga = WargaRegistrationForm(request.POST, prefix='warga')
        if account.is_valid() and warga.is_valid():

            user = account.save(commit=False)
            user.user_type = 4
            user.objects.create_user()
            warga_data = warga.save(commit=False)
            warga_data.user = user
            warga_data.save()
            return redirect('warga:login')
        else:
            return redirect('warga:login')
    else:
        account = AccountForm(prefix='account')
        warga = WargaRegistrationForm(prefix='warga')
        return render(request, 'warga/register.html', {'warga': warga, 'account': account})
