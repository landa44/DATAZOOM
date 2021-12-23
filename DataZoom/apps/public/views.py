from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


def index(request):
    posts = Post.published.all()
    return render(request, "home.html", {"posts": posts})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
