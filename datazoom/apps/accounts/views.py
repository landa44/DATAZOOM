from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def profile(request):
    return render(request, "accounts/profile.html")

def registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save(user_form=user_form)
            return redirect('/accounts/login')

    else:
        return render(request, "accounts/register.html",
            {"user_form": UserRegistrationForm(), "profile_form": UserProfileForm()})

