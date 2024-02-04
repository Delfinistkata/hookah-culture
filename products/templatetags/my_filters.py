"""
Import the 'template' module from Django.
The 'template' module in Django provides
functionality related to template rendering,
allowing developers to work with templates
in the Django web framework.
"""
from django import template

register = template.Library()

@register.filter(name='reviews_range')
def reviews_range(number=5):
    """
    Custom Django template filter
    to generate a range representing
    the number of stars for reviews.
    """
    return range(int(number))
