from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.

def indexcore(request):
    FormContact = ContactForm()

    if request.method =="POST":

        FormContact = ContactForm(data=request.POST)

        if FormContact.is_valid():

            email = request.POST.get('email','')
            tipom = request.POST.get('tipom','')
            nombre = redirect.POST.get('nombre','')
            msj = redirect.POST.get('msj','')

            FormContact.save()
            return redirect(reverse('inicio')+"?ok")
    return render(request, 'core/index.html', {'formulario':FormContact})
