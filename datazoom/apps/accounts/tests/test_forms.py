from django.test import TestCase
from ..forms import UserRegistrationForm
from ..forms import UserProfileForm
from ..forms import EMPTY_USERNAME_ERROR
from ..forms import EMPTY_FIRSTNAME_ERROR
from ..forms import EMPTY_LASTNAME_ERROR
from ..forms import EMPTY_PASSWORD_ERROR
from ..forms import NOT_MATCHING_PASSWORD_CONFIRMATION_ERROR
from ..forms import DUPLICATED_USERNAME_ERROR
from unittest import skip
from django.contrib.auth.models import User
from unittest.mock import Mock, patch


class UserProfileFormTest(TestCase):
    def test_form_input(self):
        form = UserProfileForm()
        self.assertIn('placeholder="Bio"', form.as_p())
        self.assertIn('placeholder="Website"', form.as_p())

    @patch('datazoom.apps.accounts.models.UserProfile.create_new')
    def test_form_save(self, mock_create_new):
        fake=Mock()
        data={'bio':'bla bla', 'website':'http://bla.com'}
        form = UserProfileForm(data)
        form.is_valid()
        form.save(fake)
        mock_create_new.assert_called_once_with(data['bio'], data['website'], fake)

class UserRegistrationTest(TestCase):
    def test_form_input(self):
        form = UserRegistrationForm()
        self.assertIn('placeholder="Username"', form.as_p())
        self.assertIn('placeholder="Username"', form.as_p())
        self.assertIn('placeholder="First Name"', form.as_p())
        self.assertIn('placeholder="Last Name"', form.as_p())
        self.assertIn('placeholder="Email"', form.as_p())
        self.assertIn('placeholder="Password"', form.as_p())
        self.assertIn('placeholder="Password Confirmation"', form.as_p())

    def form_validation_for(self, field, data, error_message):
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors[field], [error_message])

    def test_form_validation_for_no_username(self):
        self.form_validation_for('username', {'username':''}, EMPTY_USERNAME_ERROR)

    def test_form_validation_for_no_name(self):
        self.form_validation_for('first_name',{'first_name':''}, EMPTY_FIRSTNAME_ERROR)

    def test_form_validation_for_no_last_name(self):
        self.form_validation_for('last_name',{'last_name':''}, EMPTY_LASTNAME_ERROR)

    def test_form_validation_for_no_password(self):
        self.form_validation_for('password', {'username':'Pablo', 'password':''}, EMPTY_PASSWORD_ERROR)

    def test_form_validation_for_wrong_confirmation_password(self):
        self.form_validation_for('password2', {'username':'Pablo', 'password':'aaaa', 'password2':'dfaa'}, NOT_MATCHING_PASSWORD_CONFIRMATION_ERROR)

    def test_duplicate_usernames(self):
        user_ = User.objects.create(username='pablo')
        self.form_validation_for('username', {'username':'pablo', 'first_name':'Pablo', 'password':'aaaa', 'password2':'aaaa'}, DUPLICATED_USERNAME_ERROR)

    def test_form_save(self):
        form = UserRegistrationForm(data={'username':'pablo', 'first_name':'Pablo', 'last_name':'Alonso', 'password':'aaaa', 'password2':'aaaa'})
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user, User.objects.all()[0])
