"""
Module containing URL patterns for the 'home' app.
This module defines the URL patterns for routing
requests to views within the 'home' app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
