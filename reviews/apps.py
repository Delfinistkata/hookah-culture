"""
This module defines the configuration class
`ReviewsConfig` for the Django app 'reviews'.
It specifies the default auto field and the
name of the app. The AppConfig is used to
configure various aspects of the app,
including the default auto field for models.
"""
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    ReviewsConfig: AppConfig class for the Reviews app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
