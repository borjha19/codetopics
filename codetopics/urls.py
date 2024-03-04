"""
URL configuration for codetopics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('web', views.web, name="web"),
    path('mobile', views.mobile, name="mobile"),
    path('Embedded', views.Embedded, name="Embedded"),
    path('Math', views.Math, name="Math"),
    path('OOP_functional', views.OOP_functional, name="OOP_functional"),
    path('operating_system', views.operating_system, name="operating_system"),
    path('languages', views.languages, name="languages"),
    path('ds_alg', views.ds_alg, name="ds_alg"),
    path('accounts/profile', views.ProfileView.as_view(), name="profile"),


    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name = 'login'),

]