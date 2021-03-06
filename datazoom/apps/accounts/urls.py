from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import UserLoginForm

app_name = "accounts"

urlpatterns = [
    path(
        "login",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
    # path("login", views.user_login, name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("profile", views.profile, name="profile"),
    path("registration", views.registration, name="registration"),
]
