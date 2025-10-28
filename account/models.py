from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL 


class Profile(models.Model):

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile',
    )
    
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    full_name = models.CharField(
        max_length=255, 
        blank=True, 

    )
    bio = models.TextField(
        max_length=500, 
        blank=True, 

    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True,

    )
    
    # فیلدهای مرتبط با سفر
    location = models.CharField(
        max_length=100, 
        blank=True, 

    )
    favorite_destination = models.CharField(
        max_length=255, 
        blank=True, 

    )

    # لینک‌های شبکه‌های اجتماعی
    website_url = models.URLField(
        max_length=200, 
        blank=True, 
        null=True,

    )
    instagram_url = models.URLField(
        max_length=200, 
        blank=True, 
        null=True,

    )
    twitter_url = models.URLField(
        max_length=200, 
        blank=True, 
        null=True,

    )

    # فیلدهای مدیریتی
    is_public = models.BooleanField(
        default=True, 
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ['user__username']

    def __str__(self):
        """نمایش نام کاربری یا نام کامل کاربر"""
        return f"Profile of {self.user.username}"
    
    def save(self, *args, **kwargs):
        """
        Overridden to automatically generate a unique slug based on the user's username.
        """
     
        if not self.slug:
            self.slug = slugify(self.user.username)
        
            original_slug = self.slug
            counter = 1
            while Profile.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)


    def get_absolute_url(self):
    
        return reverse('account:profile', kwargs={'slug': self.slug})