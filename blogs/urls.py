from django.urls import path
from .views import *
from blogs import views

app_name = "blogs"

urlpatterns = [
    path("blog/",views.blog_home, name="blog_home"),
    path("blog/category/<slug:slug>/",views.blog_home, name= "category"),
    path("blog/author/<str:username>/", views.blog_home, name="author"),
    path("blog/<slug:slug>/",views.blog_single, name="blog_single"),
    
]
