from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .forms import *

def index_view(request):
    return render(request, "main/index.html")

def about_view(request):
    return render(request, "main/about.html")

def contact_view(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    