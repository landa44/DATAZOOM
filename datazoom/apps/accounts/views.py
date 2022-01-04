from django.shortcuts import render
from .forms import *

# Create your views here.
def profile(request):
  return render(request,'accounts/profile.html')

def registration(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    profile_form = UserProfileForm(request.POST)

    if user_form.is_valid() and profile_form.is_valid():
    # Create a new user object but avoid saving it yet
      new_user = user_form.save(commit=False)
    # Set the chosen password
      new_user.set_password(
      user_form.cleaned_data['password'])
    # Save the User object
      new_user.save()

      new_profile = profile_form.save(commit=False)
      new_user.user = new_user
      new_profile.save()

      return render(request,'accounts/profile.html')
  else:
    user_form = UserRegistrationForm()
    profile_form = UserProfileForm()

  return render(request,
    'accounts/register.html',
    {'user_form': user_form, 'profile_form': profile_form})