from django.shortcuts import render

def profile(request):
    return render(request, 'accounts/profile.html')

def upload(request):
    return render(request, 'accounts/upload.html')

def logout(request):
    return render(request, 'accounts/logout.html')
