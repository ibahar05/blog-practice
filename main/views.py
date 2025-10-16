from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages

def index_view(request):
    return render(request, "main/index.html")

def about_view(request):
    return render(request, "main/about.html")

def contact_view(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "message": "Your message has been sent successfully✅"
                })

            # ✅ اگر معمولی بود (رفرش صفحه)
            messages.success(request, "Your message has been sent successfully✅")
            return redirect("main:contact")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": False,
                    "message": "Please fill in all fields correctly "
                })

            messages.error(request, "Please fill in all fields correctly ❌")
            return redirect("main:contact")

    form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ You have successfully subscribed to the newsletter!")
            # پاسخ برای AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': "You have successfully subscribed!"})
            return redirect('/')
        else:
            messages.error(request, "❌ Invalid email address.")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': "Invalid email address."})
            return HttpResponseRedirect('/')