from django.urls import path
from .views import *
from main import views

app_name = "main"
urlpatterns = [
    path("",views.index_view, name="index"),
    path("about/",views.about_view, name="about"),
    path("contact/",views.contact_view, name="contact"),
    path("newsletter/",views.newsletter_view, name = "newsletter"),
]
