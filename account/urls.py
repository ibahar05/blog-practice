from django.urls import path, reverse_lazy
from .views import *
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path('register/', AuthView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),

    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html",
            email_template_name='account/password_reset_email.html',
            success_url=reverse_lazy('account:password_reset_done')
        ),
        name='password_reset'
    ),

    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name='password_reset_done'
    ),

    path(
        'password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html",
            success_url=reverse_lazy('account:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),

    path(
        'password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name='password_reset_complete'
    ),


    path('profile/<slug:slug>/', views.profile_detail, name='profile'),

    

]