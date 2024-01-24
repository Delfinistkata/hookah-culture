from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Review


@login_required
def show_reviews(request):
    """ A view to show the user's product reviews """
    reviews = Review.objects.filter(author=request.user)

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)