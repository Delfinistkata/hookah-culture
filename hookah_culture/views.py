"""
Django Shortcuts - Render Function
Renders a Django template to an
HttpResponse object with a given context.
"""
from django.shortcuts import render


def handler404(request, exception):
    """
    Error Handler 404 - Page Not Found
    """
    return render(request, "errors/404.html", status=404)
