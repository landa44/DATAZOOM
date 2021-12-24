from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "public"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
urlpatterns += staticfiles_urlpatterns()




