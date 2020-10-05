from django.shortcuts import render
from . models import Contact
from . import forms
from django.views.generic import(TemplateView,ListView)
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
     
    template_name = 'about.html'

def Contact(request):
    form = forms.Contact(request.POST)

    if form.is_valid():
        #Do something code
        print("Validation success!")
        print("NAME: " + form.cleaned_data['name'])
        print("PHONE: " + form.cleaned_data['phone'])
        print('Email: ' + form.cleaned_data['email'])
        print('Content: ' + form.cleaned_data['content'])
    
    return render(request, "Home/contact.html",{'form':form})

