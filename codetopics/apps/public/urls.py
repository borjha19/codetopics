from django.urls import path

from . import views

app_name="public"
urlpatterns = [
    path('', views.index, name="index"),
    path('web', views.web, name="web"),
    path('mobile', views.mobile, name="mobile"),
    path('Embedded', views.Embedded, name="Embedded"),
    path('ds_alg', views.ds_alg, name="ds_alg"),
    path('languages', views.languages, name="languages"),

]