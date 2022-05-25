from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "blog"

urlpatterns = [
    path("recents/", views.get_recents_posts, name="recents"),
    #   path('blog/', views.get_post),
]
urlpatterns += staticfiles_urlpatterns()
