"""
Module for configuring the 'home' app in a Django project.
This module defines an AppConfig class, HomeConfig, which specifies the configuration
settings for the 'home' app.
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the 'home' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
