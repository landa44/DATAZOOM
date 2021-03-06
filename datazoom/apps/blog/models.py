from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    class Meta:
        ordering = ("-publish",)

        def __str__(self):
            return self.title

class Tag(models.Model):
    objects = models.Manager()
    tag_name = models.CharField(max_length=60)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-tag_name",)

        def __str__(self):
            return self.tag_name

class Interest(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, 
                            related_name='interests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                            related_name='interests')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)