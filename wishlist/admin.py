"""
Django admin configuration for the Wishlist model.
This module defines the configuration for
the Django admin interface related to the Wishlist model.
It specifies the display fields, ordering,
and other settings for the Wishlist model in the admin interface.
"""
from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin configuration for Wishlist model.
    It defines how the Wishlist model is displayed and managed
    in the Django admin interface.
    """
    model = Wishlist
    fields = ('user_profile', 'product')
    list_display = ('pk', 'user_profile', 'product')


admin.site.register(Wishlist, WishlistAdmin)
