from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]