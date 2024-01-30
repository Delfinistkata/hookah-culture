"""
Django AppConfig for the 'profiles' app.
This module defines the AppConfig class for the 'profiles' app. AppConfig
is a configuration class for the Django application and provides metadata
and configuration for the app.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    AppConfig for the 'profiles' app.
    This AppConfig defines configuration settings for the 'profiles' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
