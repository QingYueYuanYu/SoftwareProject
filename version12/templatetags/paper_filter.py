from django import template
from django.template.defaultfilters import stringfilter


# Create filter
register = template.Library()
@register.filter(is_safe=True)
@stringfilter
def spacify(value):
    return value