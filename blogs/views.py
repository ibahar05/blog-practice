from django.shortcuts import render

def blog_home(request):
    return render(request,"blogs/blog_home.html")
