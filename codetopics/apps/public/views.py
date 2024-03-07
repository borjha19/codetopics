from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def web(request):
    return render(request, 'Web.html')

def mobile(request):
    return render(request, 'mobile.html')

def Embedded(request):
    return render(request, 'embedded.html')

def languages(request):
    return render(request, 'languages.html')

def ds_alg(request):
    return render(request, 'ds_alg.html')

