from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError

EMPTY_USERNAME_ERROR = "You should type a Username!"
EMPTY_FIRSTNAME_ERROR = "You should have a name, right?"
EMPTY_LASTNAME_ERROR = "You don't have parents or what?"
EMPTY_PASSWORD_ERROR = "You should set up a Password!"
NOT_MATCHING_PASSWORD_CONFIRMATION_ERROR = "Confirmation password does not match!"
DUPLICATED_USERNAME_ERROR = 'This username is already in use!'

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )


class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
        error_messages={'required': EMPTY_PASSWORD_ERROR}, 
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password Confirmation"}
        ),
    )
 
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
        }

        error_messages = {
            'username': {'required': EMPTY_USERNAME_ERROR},
            'first_name': {'required': EMPTY_FIRSTNAME_ERROR},
            'last_name' : {'required': EMPTY_LASTNAME_ERROR}
        }  

    def validate_unique(self):
        try: 
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'username' : [DUPLICATED_USERNAME_ERROR]}
            self._update_errors(e)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError(NOT_MATCHING_PASSWORD_CONFIRMATION_ERROR)
        return cd["password2"]

    def save(self):
        cd = self.cleaned_data
        new_user = User(username=cd["username"], first_name=cd["first_name"], email=cd["email"])
        new_user.set_password(cd["password"])
        new_user.save(force_insert=True)
        return new_user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["website", "bio"]

        widgets = {
            "website": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "Website"}
            ),
            "bio": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Bio"}
            ),
        }
    
    def save(self, owner):
        return UserProfile.create_new(self.cleaned_data['bio'],
                                        self.cleaned_data['website'],
                                        owner)
