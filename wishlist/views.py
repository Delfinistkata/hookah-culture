from django.shortcuts import render

from profiles.models import UserProfile
from .models import Wishlist



def wishlist(request):
    """ A view to return the wishlist page """

    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    return render(
        request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist}
    )
