from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter

def urlify(value):
    return urlparse(value)