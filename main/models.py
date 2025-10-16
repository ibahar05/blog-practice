from django.db import models
from datetime import timezone

class Contact(models.Model):

    class Status(models.TextChoices):
        NEW = 'new', 'New'
        READ = 'read', 'Read'
        RESPONDED = 'responded', 'Responded'
        ARCHIVED = 'archived', 'Archived'

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField( max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        "Status",
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.name} - {self.subject[:30]}"
    



class Newsletter(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'
        UNSUBSCRIBED = 'unsubscribed', 'Unsubscribed'

    email = models.EmailField(
        "Email Address",
        unique=True,
        db_index=True,
        help_text="Subscriber's email address"
    )
    status = models.CharField(
        "Status",
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    subscribed_at = models.DateTimeField(
        "Subscribed At",
        auto_now_add=True
    )
    unsubscribed_at = models.DateTimeField(
        "Unsubscribed At",
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return f"{self.email} ({self.get_status_display()})"