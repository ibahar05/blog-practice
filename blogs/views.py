from django.shortcuts import get_object_or_404, render
from .models import *

def blog_home(request):
    posts=Post.objects.filter(status="published")
    context={
        "posts":posts
    }
    return render(request,"blogs/blog_home.html", context)

def blog_single(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    context={
        "post":post
    }
    return render(request,"blogs/blog_single.html", context)