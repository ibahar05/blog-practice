from django.shortcuts import get_object_or_404, render
from .models import *

def blog_home(request, slug=None,username=None):
    posts=Post.objects.filter(status="published")

    category = None
    author = None

    if slug:  # اگر slug دسته داده شده
        category = get_object_or_404(Category, slug=slug)
        posts = posts.filter(category=category)

    if username:
        author = get_object_or_404(User, username=username)
        posts = posts.filter(author=author)

    
    context={
        "posts":posts,
        "category":category,
        "author": author,
    }
    return render(request,"blogs/blog_home.html", context)

#-------------------------------------------------------------------------------

def blog_single(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    context={
        "post":post
    }
    return render(request,"blogs/blog_single.html", context)

#--------------------------------------------------------------------------------

def blog_search(request):
    posts=Post.objects.filter(status="published")
    if request.method =="GET":
        posts = posts.filter(content__contains=request.GET.get("s"))


    context = {"posts":posts}
    return render(request, "blogs/blog_home.html", context)

