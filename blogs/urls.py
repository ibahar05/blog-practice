from django.urls import path
from .views import *
from blogs import views

app_name = "blogs"

urlpatterns = [
    path("blog/",views.blog_home, name="blog_home"),
    path("blog/<slug:slug>/",views.blog_single, name="blog_single"),
]
