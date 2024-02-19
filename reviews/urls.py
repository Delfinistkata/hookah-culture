"""
Django URL patterns for handling reviews.
This module defines URL patterns for views
related to user reviews, including
showing reviews, adding a new review,
editing an existing review, and deleting a review.
"""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_reviews, name='reviews'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path(
        'edit_review/<int:review_id>/',
        views.edit_review,
        name='edit_review'
    ),
    path(
        'delete_review/<int:review_id>/',
        views.delete_review,
        name='delete_review'
    ),
]
