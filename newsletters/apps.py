"""
Newsletters App
This module defines the configuration for the 'newsletters' app.
"""
from django.apps import AppConfig


class NewslettersConfig(AppConfig):
    """
    AppConfig for the 'newsletters' app.
    This AppConfig defines configuration settings for the 'newsletters' app,
    including the default_auto_field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletters'
