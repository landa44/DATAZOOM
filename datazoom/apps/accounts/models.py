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

    # is_graduate = models.BooleanField(default =True)
    # is_student = models.BooleanField(default =True)
    # study_place = models.CharField(max_length=50, blank=True, null=True)

    # is_working = models.BooleanField(default=True)
    # work_place = models.CharField(max_length=50, blank=True, null=True)
