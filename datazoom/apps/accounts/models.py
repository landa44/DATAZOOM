from django.db import models
from django.contrib.auth.models import User

# from datazoom.apps.blog import models as blog_models

# Create your models here.


class UserProfile(models.Model):
    # owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # settings
    is_full_named_displayed = models.BooleanField(default=True)

    # details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    @staticmethod
    def create_new(bio, website, owner):
        return UserProfile.objects.create(bio=bio, website=website, user=owner)
    