"""
This module defines the models used in the application.
It includes the 'Subscriber' model representing newsletter subscribers.
"""
from django.db import models


class Subscriber(models.Model):
    """
    This model represents subscribers who have opted to receive newsletters.
    It includes fields for the subscriber's email address and the date they
    were added to the subscriber list.
    """

    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Subscriber object.
        Returns the email address of the subscriber.
        """
        return str(self.email)
