from django.shortcuts import render, redirect
from codetopics.apps.accounts.forms import UploadForm
from codetopics.apps.public.models import recentQuery


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
                category = form.cleaned_data["category"]

                query = recentQuery()
                query.register_upload(url=url)
                if media == '1':
                    query.add_video(url=url, title=title, category=category)
                elif media == '2':
                    query.add_photo(url=url, title=title, category=category)
                elif media == '3':
                    query.add_article(url=url, title=title, category=category)

                               
                if category =='1':
                    return redirect('http://127.0.0.1:8000/web')
                elif category == '2':
                    return redirect('http://127.0.0.1:8000/Embedded')
                elif category == '3':
                    return redirect('http://127.0.0.1:8000/ds_alg')
                else:
                    return redirect('http://127.0.0.1:8000/languages')

        else:
            return render(request, 'accounts/upload.html', {'form':form})
    else:
        form = UploadForm(request.POST)

    return render(request, 'accounts/upload.html', {'form': form})


