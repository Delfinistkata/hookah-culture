from django import template

register = template.Library()

@register.filter(name='reviews_range')
def reviews_range(number=5):
    return range(int(number))