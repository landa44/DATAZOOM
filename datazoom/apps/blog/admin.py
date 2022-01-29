from re import search
from django.contrib import admin
from .models import Interest, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    list_filter = ('tag_name', 'created')
    search_fields = ('tag_name',)
    date_hierarchy = "created"
    ordering = ('tag_name',)

@admin.register(Interest)
class InterstAdmin(admin.ModelAdmin):
    list_display = ('tag', 'user', 'created')
    list_filter = ('tag', 'user', 'created')
    search_fields = ('tag', 'user')
    raw_id_fields = ("user", 'tag')
    date_hierarchy = "created"
    ordering = ('user', 'tag')