"""
Admin configuration for the Subscriber model.
This module registers the Subscriber model with the Django admin site
and defines the custom configuration for displaying and ordering the
Subscriber records.
"""
from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    """
    This class defines the custom configuration for displaying and ordering
    Subscriber records in the Django admin site.
    """
    list_display = ('email', 'is_subscribed', 'date_added')

    ordering = ('-date_added',)

admin.site.register(Subscriber, SubscriberAdmin)
