"""
URL patterns for the checkout app.
This module defines URL patterns for
the views related to the checkout process
and the webhook endpoint. These patterns 
include paths for displaying the checkout,
success page, caching checkout data,
and handling webhooks.
"""
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
