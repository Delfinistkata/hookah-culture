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


@register.filter(name='is_wishlisted')
def is_wishlisted(wishlists, profile_id):
    """
    Custom Django template filter
    to detect if the product is in the wishlist
    of the current user.
    """
    return wishlists.filter(user_profile_id=profile_id).exists()
