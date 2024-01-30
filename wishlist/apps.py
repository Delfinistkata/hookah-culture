"""
Django AppConfig module for application-specific configuration.
"""
from django.apps import AppConfig


class WishlistConfig(AppConfig):
    """
    Configuration for the Wishlist app.
    It defines the configuration for the Wishlist app, including
    settings such as the default auto field and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wishlist'

    def ready(self):
        import wishlist.signals
