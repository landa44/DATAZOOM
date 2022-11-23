from django.test import TestCase

from unittest.mock import patch
from unittest.mock import patch, call

@patch('datazoom.apps.accounts.views.UserRegistrationForm')
@patch('datazoom.apps.accounts.views.UserProfileForm')
class RegistrationViewTest(TestCase):
    def test_redirects_to_login_page(self, mockUserProfileForm , mockUserRegistrationForm):
        registration_form = mockUserRegistrationForm.return_value
        registration_form.is_valid.return_value = True

        profile_form = mockUserProfileForm.return_value
        profile_form.is_valid.return_value = True

        response = self.client.post('/accounts/registration')

        self.assertRedirects(response, "/accounts/login")

    def test_save_form_if_form_is_valid(self, mockUserProfileForm , mockUserRegistrationForm):
        registration_form = mockUserRegistrationForm.return_value
        registration_form.is_valid.return_value = True

        profile_form = mockUserProfileForm.return_value
        profile_form.is_valid.return_value = True  

        self.client.post('/accounts/registration')
        profile_form.save.assert_called_once_with(user_form=registration_form)
                    