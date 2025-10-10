from django import template
from blogs.models import *
from django.utils.timesince import timesince
from django.utils.timezone import now

register = template.Library()

@register.inclusion_tag("blogs/blog_popular_posts.html")
def latestposts():
    posts=Post.objects.filter(status="published").order_by("published_date")[:2]
    return {"posts":posts}



@register.filter
def timesince_simple(value):
    if not value:
        return ""
    return timesince(value, now()).split(",")[0]