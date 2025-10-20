from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
#-----------------------------------------------------------------------------------------

class Post(models.Model):
    """
    The main model for a blog or article post.
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    # Core Content Fields
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    content = models.TextField()
    summary = models.TextField(max_length=500, blank=True)
    counted_view = models.IntegerField(default=0)

    # Relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='posts')
    tags = TaggableManager()

    # Metadata and Management
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        constraints = [
            # Ensure published posts have a published_date set
            models.CheckConstraint(
                check=models.Q(status='draft') | models.Q(published_date__isnull=False),
                name='published_posts_must_have_published_date'
            )
        ]

    def __str__(self):
        return self.title

    # Model Methods
    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically generate a unique slug.
        Also sets the published_date if the status is set to 'published'
        and the published_date is not already set.
        """
        # Auto-generate slug
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure slug is unique, appending a counter if necessary
            original_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        # Handle published_date
        if self.status == 'published' and not self.published_date:
            from django.utils import timezone
            self.published_date = timezone.now()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the canonical URL for a Post object. Requires URL configuration.
        """
        return reverse('blogs:blog_single', kwargs={'slug': self.slug})
    
    # def clean(self):
    #     if self.status == 'published' and not self.published_date:
    #         raise ValidationError("published posts must have published date")