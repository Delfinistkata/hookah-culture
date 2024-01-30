"""
URL patterns for the 'profiles' app.
This module defines the URL patterns for the views related to user profiles
in the 'profiles' app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]
