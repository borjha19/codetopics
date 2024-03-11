from django.shortcuts import render
from codetopics.apps.accounts.models import profile
from django.contrib.auth.models import User
from codetopics.apps.accounts.forms import UploadForm

def index(request):
    if request.user.is_authenticated:
        Profile = profile.objects.get(id=(request.user.id))
        interests = Profile.interests.all()
        return render(request, 'index.html', {'Interests': interests})
    else:
        return render(request, 'index.html')


def web(request):
    if request.user.is_authenticated:  
        return render(request, 'Web.html')
    else:
        return render(request, 'Web.html')

def mobile(request):
    return render(request, 'mobile.html')

def Embedded(request):
    return render(request, 'embedded.html')

def languages(request):
    return render(request, 'languages.html')

def ds_alg(request):
    return render(request, 'ds_alg.html')

