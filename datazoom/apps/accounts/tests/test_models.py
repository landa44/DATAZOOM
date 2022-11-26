from django.test import TestCase
from ..models import UserProfile
from django.contrib.auth.models import User

class UserProfileTest(TestCase):
    def test_profile_is_related_to_user(self):
        user = User.objects.create()
        profile = UserProfile()
        profile.user = user
        profile.save()
        self.assertEqual(profile, user.profile)

    def test_cannot_save_with_no_user(self):
        profile = UserProfile()
        with self.assertRaises(Exception):
            profile.save()
            profile.full_clean()

    def test_duplicate_profile_invalid(self):
        user = User.objects.create()
        profile1 = UserProfile()
        profile1.user = user
        profile1.save()

        with self.assertRaises(Exception):
            profile2 = UserProfile()
            profile2.user = user
            profile2.save()

    def test_create_new_create_new_instance(self):
        user = User.objects.create()
        profile = UserProfile.create_new('A bio', 'http//:myweb.com', user)
        self.assertEqual(profile, UserProfile.objects.all()[0])
