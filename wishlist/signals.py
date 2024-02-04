"""
Signal handler for creating a Wishlist when the first item is added.
This signal handler is connected to the post_save signal of the Wishlist model.
When a new Wishlist item is created (i.e., a product is added to the wishlist),
this handler checks if the user already has a Wishlist. If not, it creates a new
Wishlist for the user with the added product.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wishlist


@receiver(post_save, sender=Wishlist)
def create_wishlist_on_first_item_added(sender, instance, created, **kwargs):
    """
    Creates a new Wishlist for the user when the first item is added.
    """
    if created:
        user_profile = instance.user_profile
        if not user_profile.user_wishlist.exists():
            # Create a new Wishlist for the user if they don't have one
            Wishlist.objects.create(
                user_profile=user_profile, product=instance.product)
