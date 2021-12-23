from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def get_recents_posts(request):
    query_result = Post.objects.filter(status="published").order_by('-updated')
    posts = query_result[0:min(len(query_result),5)]
    return render(request, "home.html",{'posts': posts})

