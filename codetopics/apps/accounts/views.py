from django.shortcuts import render, redirect
from codetopics.apps.accounts.forms import UploadForm
from codetopics.apps.accounts.models import recentQuery, VideoUploadedEvent, PhotoUploadedEvent, ArticleUploadedEvent, profile


def profile(request):
    return render(request, 'accounts/profile.html')

def upload(request):
    if request.method == 'POST':
        form =  UploadForm(request.POST)
        if form.is_valid():
            if 'submit' in request.POST:
                url = form.cleaned_data["URL"]
                media = form.cleaned_data["media"]
                title = form.cleaned_data["title"]
                topic = form.cleaned_data["topic"]
                category = form.cleaned_data["category"]

                profileId = request.user.id
                query = recentQuery(env= {
                    "PERSISTENCE_MODULE": "eventsourcing_django",
                })
                query.register_upload(profileId=profileId)
                if media == '1':
                    query.add_video(url=url, profileId=profileId, title=title, category=topic)
                elif media == '2':
                    query.add_photo(url=url, profileId=profileId, title=title, category=topic)
                elif media == '3':
                    query.add_article(url=url, profileId=profileId, title=title, category=topic)
                    
                list = query.get_events(profileId)
                if topic =='1':
                    web_list = []
                    
                    for obj in list:
                        if obj.category == '1':
                            web_list.append(obj)
            
                    return render(request, 'Web.html', {'web_list':web_list})
                elif topic == '2':
                    mobile_list = []
                    
                    for obj in list:
                        if obj.category == '2':
                            mobile_list.append(obj)
            
                    return render(request, 'mobile.html', {'mobile_list':mobile_list})
                elif topic == '3':
                    Embedded_list = []
                    
                    for obj in list:
                        if obj.category == '3':
                            Embedded_list.append(obj)
            
                    return render(request, 'Embedded.html', {'Embedded_list':Embedded_list})
                elif topic == '4':
                    ds_list = []
                    
                    for obj in list:
                        if obj.category == '4':
                            ds_list.append(obj)
            
                    return render(request, 'ds_alg.html', {'ds_list':ds_list})
                else:
                    languages_list = []
                    
                    for obj in list:
                        if obj.category == '5':
                            languages_list.append(obj)
            
                    return render(request, 'languages.html', {'languages_list':languages_list})

        else:
            return render(request, 'accounts/upload.html', {'form':form})
    else:
        form = UploadForm(request.POST)

    return render(request, 'accounts/upload.html', {'form': form})


