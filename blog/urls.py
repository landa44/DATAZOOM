from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index),
    path('hello/', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
 #   path('blog/', views.get_post),
]
urlpatterns += staticfiles_urlpatterns()