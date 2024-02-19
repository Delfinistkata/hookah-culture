"""
This module contains the Contact model,
which represents messages sent by users.
"""
from django.db import models


class Contact(models.Model):
    """
    Users can send messages through the contact form,
    and the model represents each message.
    """
    # Set topic options for message
    TOPIC_CHOICES = [
        ('Order', 'Order Inquiry'),
        ('Product', 'Product Inquiry'),
        ('General Inquiry', 'General Inquiry'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    topic = models.CharField(max_length=15, choices=TOPIC_CHOICES)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Pending',
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Set ordering and plural name options
        for the Contact model.
        """
        ordering = ['-date_created']
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        """
        String representation of the Contact object.
        Returns a formatted string displaying the sender's name.
        """
        return f'Message from {self.name}'
