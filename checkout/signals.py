"""
Signal handlers for updating order total
on changes to OrderLineItem instances.
This module includes signal handlers that 
respond to post_save and post_delete
events on the OrderLineItem model.
The handlers ensure that the order total is
updated when line items are created, updated, or deleted.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """ 
    Update order total on lineitem delete 
    """
    instance.order.update_total()
