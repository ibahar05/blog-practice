from django import template
from blogs.models import *
from django.utils.timesince import timesince
from django.utils.timezone import now

from django.db.models import Count, Q
from blogs.models import Category


register = template.Library()

@register.inclusion_tag("blogs/blog_popular_posts.html")
def latestposts():
    posts=Post.objects.filter(status="published").order_by("published_date")[:2]
    return {"posts":posts}

#-------------------------------------------------------------------------------------

@register.filter
def timesince_simple(value):
    if not value:
        return ""
    return timesince(value, now()).split(",")[0]

#-------------------------------------------------------------------------------------

@register.inclusion_tag("blogs/blog_category.html")
def postcategory():
    """
    برمی‌گرداند همه‌ی دسته‌ها به همراه تعداد پست‌های منتشرشده در هر دسته.
    """
    categories = Category.objects.annotate(
        post_count=Count('posts', filter=Q(posts__status='published')))

    
    
    return {"categories": categories}