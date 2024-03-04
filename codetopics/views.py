from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')

def web(request):
    return render(request, 'Web.html')

def mobile(request):
    return render(request, 'mobile.html')

def Embedded(request):
    return render(request, 'embedded.html')

def Math(request):
    return render(request, 'Math.html')

def OOP_functional(request):
    return render(request, 'OOP_functional.html')

def operating_system(request):
    return render(request, 'operating_system.html')

def languages(request):
    return render(request, 'languages.html')

def ds_alg(request):
    return render(request, 'ds_alg.html')

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name='accounts/profile.html'


