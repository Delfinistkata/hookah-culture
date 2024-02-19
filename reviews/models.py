"""
Django models for handling reviews.
This module defines models related
to user reviews, including the Review model.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Review model representing a user review for a product.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product_reviews'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        """
        Orders reviews by their creation timestamp in descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        __str__: Returns a formatted string representation of the review.
        """
        return f'{self.product} review by {self.author}'
