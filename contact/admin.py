"""
This module contains the admin configuration for the 'Contact' model.
"""
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact administration:
    This class defines the administration settings for the Contact model.
    It specifies the displayed fields in the list view, filters, and ordering.
    """
    list_display = (
        "date_created",
        "topic",
        "name",
        "email",
        "message",
        "status",
    )

    list_filter = ("date_created", "name", "topic", "status")

    ordering = ("-date_created",)
