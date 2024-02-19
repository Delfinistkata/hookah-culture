"""
Django models import statements.
This module includes import statements
for Django models related to database interactions.
It imports the 'models' module from 'django.db'
for defining database models, and the 'Avg' aggregation
function from 'django.db.models' for calculating averages.
"""
from django.db import models
from django.db.models import Avg


class Category(models.Model):
    """
    Model representing a product category.
    """
    class Meta:
        """
        Metadata options for the Category model.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the category.
        """
        return str(self.name)

    def get_friendly_name(self):
        """
        Return the friendly name of the category.
        """
        return self.friendly_name


class Product(models.Model):
    """
    Model representing a product.
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    @property
    def rating(self):
        """
        Calculate and return the average
        rating of the product based on reviews.
        """
        return self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return str(self.name)
