"""
Django models import statements for UserProfile and Wishlist.
"""
from profiles.models import UserProfile
from .models import Wishlist


def wishlist_items(request):
    """
    Wishlist items context processor.
    It retrieves the wishlist items for the currently
    authenticated user and provides them as a context variable.
    """
    wishlist_items = []

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        wishlist_items = Wishlist.objects.filter(user_profile=user_profile)

    return {
        'user_wishlist': wishlist_items,
    }
