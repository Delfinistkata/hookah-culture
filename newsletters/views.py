"""
This module contains views related to the newsletters app, 
such as adding subscribers.
"""
from django.http import HttpResponseRedirect

from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm


def add_subscriber(request):
    """
    Add email to the subscriber list.
    This view function handles the addition of an email address to the subscriber list.
    It uses the SubscriberForm to validate and save the email address.
    If the email already exists in the database, an error message is displayed.
    Otherwise, the email is saved, and a success message is shown.
    """
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(
                request,
                f"{instance.email} already exists in our database. "
                "Please check your email and try again."
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        instance.save()
        messages.success(
            request,
            f"{instance.email} has been added to our the newsletter"
        )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
