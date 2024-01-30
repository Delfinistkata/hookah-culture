"""
This module defines the URL patterns for the 'newsletters' app, specifying how
different paths map to views provided in the 'views' module.
"""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.add_subscriber, name='newsletters'),
]
