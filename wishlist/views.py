"""
Django views for Wishlist functionality.
The views handle user wishlist operations, such as displaying the wishlist,
adding a product to the wishlist, and removing a product from the wishlist.
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


@login_required
def wishlist(request):
    """
    View to return the wishlist page.
    Retrieves the user's wishlist and paginates the results for display.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    items_per_page = 6
    paginator = Paginator(user_wishlist, items_per_page)
    page = request.GET.get('page')

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)

    return render(
        request,
        'wishlist/wishlist.html',
        {'user_wishlist': current_page, 'paginator': paginator}
    )


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.
    Checks if the product is already in the user's wishlist and adds it if not.
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    # Check if the product is already in the users wishlist
    if Wishlist.objects.filter(
        user_profile=user_profile,
        product=product
    ).exists():
        messages.warning(
            request, f'{product.name} is already in your Wishlist.')
    else:
        # create a new wishlist item
        wishlist_item = Wishlist.objects.create(
            user_profile=user_profile, product=product)
        messages.success(
            request,
            f'{wishlist_item.product.name} added to Wishlist successfully!'
        )

    # Redirect to the product detail page
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove item from Wishlist when remove icon is clicked.
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(
        user_profile=user_profile,
        product=product
    )
    wishlist_item.delete()
    messages.success(request, f'{product.name} has been successfully removed.')
    return redirect(reverse('wishlist'))
