from django.shortcuts import render
from codetopics.apps.accounts.models import profile
from django.contrib.auth.models import User
from codetopics.apps.accounts.models import recentQuery

def index(request):
    if request.user.is_authenticated:
        Profile = profile.objects.get(id=(request.user.id))
        interests = Profile.interests.all()
        return render(request, 'index.html', {'Interests': interests})
    else:
        return render(request, 'index.html')


def web(request):
    if request.user.is_authenticated: 
        query = recentQuery(env= {
                    "PERSISTENCE_MODULE": "eventsourcing_django",
        })
        list = query.get_events(profileId=request.user.id)
        web_list = []
                
        for obj in list:
            if obj.category == '1':
                web_list.append(obj)
            
        return render(request, 'Web.html', {'web_list':web_list})
    else:
        return render(request, 'Web.html')

def mobile(request):
    if request.user.is_authenticated: 
        query = recentQuery() 
        list = query.get_events(profileId=request.user.id)
        mobile_list = []
                
        for obj in list:
            if obj.topic == '2':
                mobile_list.append(obj)
            
        return render(request, 'mobile.html', {'mobile_list':mobile_list})
    else:
        return render(request, 'mobile.html')

def Embedded(request):
    if request.user.is_authenticated: 
        query = recentQuery() 
        list = query.get_events(profileId=request.user.id)
        embedded_list = []
                
        for obj in list:
            if obj.topic == '3':
                embedded_list.append(obj)
            
        return render(request, 'embedded.html', {'embedded_list':embedded_list})
    else:
        return render(request, 'embedded.html')

def languages(request):
    if request.user.is_authenticated: 
        query = recentQuery() 
        list = query.get_events(profileId=request.user.id)
        languages_list = []
                
        for obj in list:
            if obj.topic == '4':
                languages_list.append(obj)
            
        return render(request, 'languages.html', {'languages_list':languages_list})
    else:
        return render(request, 'languages.html')

def ds_alg(request):
    if request.user.is_authenticated: 
        query = recentQuery() 
        list = query.get_events(profileId=request.user.id)
        ds_alg_list = []
                
        for obj in list:
            if obj.topic == '5':
                ds_alg_list.append(obj)
            
        return render(request, 'ds_alg.html', {'ds_alg_list':ds_alg_list})
    else:
        return render(request, 'ds_algs.html')

