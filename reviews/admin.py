"""
This module defines the custom
administration configuration for the Review model
in the Django admin interface.
It specifies the fields to display in the list view
and the default ordering.
This customization enhances the appearance and behavior
of the Review model in the admin interface.
"""
from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Custom administration configuration
    for the Review model.
    """
    list_display = (
        'title',
        'author',
        'product',
        'created_on',
        'rating',
    )

    ordering = ('-created_on',)


admin.site.register(Review, ReviewAdmin)
