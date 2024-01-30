"""
This module contains URL patterns for the contact app.
The URL patterns include paths for displaying the contact form 
and handling contact form submissions.
The 'contact' path is associated with the 'contact' view, 
and the 'contact_success' path is associated
with the 'contact_success' view.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
]
