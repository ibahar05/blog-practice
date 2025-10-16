from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'colored_status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    # رنگ‌دهی به وضعیت
    def colored_status(self, obj):
        color_map = {
            'new': 'red',
            'read': 'orange',
            'responded': 'green',
            'archived': 'gray',
        }
        color = color_map.get(obj.status, 'black')
        return format_html(
            '<b><span style="color: {};">{}</span></b>',
            color,
            obj.get_status_display()
        )
    colored_status.short_description = "Status"




@admin.register(Newsletter)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'status', 'subscribed_at', 'unsubscribed_at')
    list_filter = ('status',)
    search_fields = ('email',)
    ordering = ('-subscribed_at',)
