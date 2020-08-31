from django.shortcuts import render
from .forms import WargaRegistrationForm
from account.forms import AccountForm
from django.db import transaction
# Create your views here.
def login(request):
    return render(request, "warga/login.html")

@transaction.atomic
def register(request):
    account_form = AccountForm(request.POST or None, instance=request.user)
    warga_form = AccountForm(request.POST or None, instance=request.user)
    # warga_form = WargaRegistrationForm(request.POST or None, instance=request.user.Warga)
    if account_form.is_valid() and warga_form.is_valid():
        account_form.save()
        warga_form.save()
        # warga_form = WargaRegistrationForm()
        account_form = AccountForm()
        warga_form = AccountForm()
    context = {
        "warga_form" : warga_form,
        "account_form" : account_form
    }
    return render(request, "warga/register.html", context)