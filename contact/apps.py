"""
This module contains the configuration for the 'contact' app.
"""
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    AppConfig for the 'contact' app.
    This AppConfig defines configuration settings for the 'contact' app,
    including the default_auto_field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
