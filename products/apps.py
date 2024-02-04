"""
Django application configuration for the 'products' app.
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    This AppConfig class provides configuration
    settings for the 'products' app, including
    the default auto field and the app's name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
