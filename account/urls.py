from django.urls import path
from .views import *
from . import views

app_name = "account"

urlpatterns = [
    path('register/', AuthView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
]