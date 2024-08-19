from django import template

register = template.Library()

@register.filter
def range(value):
    return range(value)
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return ''
    