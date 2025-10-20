from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.contrib import messages
from django.views import View

from account.forms import SignUpForm, SignInForm

class AuthView(View):
    template_name = "account/register.html"

    def get(self, request):
        context = {
            'signup_form': SignUpForm(),
            'signin_form': SignInForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if 'signup' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                messages.success(request, f"Welcome, {user.username}! 🎉")
                return redirect('main:index')
            else:
                context = {'signup_form': form, 'signin_form': SignInForm()}
                return render(request, self.template_name, context)

        elif 'signin' in request.POST:
            form = SignInForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                messages.success(request, f"Welcome back, {form.get_user().username}! 👋")
                return redirect('main:index')
            else:
                context = {'signup_form': SignUpForm(), 'signin_form': form}
                return render(request, self.template_name, context)

        return redirect('account:register')


def logout_view(request):
    logout(request)
    return redirect('main:index')
