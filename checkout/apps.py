"""
Django application configuration for the 'checkout' app.
It specifies the default auto field for
models and includes a 'ready' method
to import signals when the application is ready.
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration class for the 'checkout' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Method called when the application is ready.
        """
        import checkout.signals
