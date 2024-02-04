"""
Custom template tags for Django app.
"""
from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a product
    based on its price and quantity.
    """
    return price * quantity
