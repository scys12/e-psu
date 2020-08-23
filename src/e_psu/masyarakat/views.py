from django.shortcuts import render
from .forms import RegisterUserForm
# Create your views here.
def masyarakat_create_view(request):
    form = RegisterUserForm(request.POST or None)
    template_name = "masyarakat/register.html"
    if form.is_valid():
        print(form.cleaned_data)
        # form.save()
        form = RegisterUserForm()    
    context = {
        "form" : form
    }
    return render(request, template_name, context)