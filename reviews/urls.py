from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_reviews, name='reviews'),
]