"""
Import Django admin and models for Product and Category.
This import statement brings in the necessary components
from Django for working with the Django admin interface
and the Product and Category models defined in the
current application.
"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Product model.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stock',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Category model.
    """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)

# Register the models and their corresponding admin options
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
