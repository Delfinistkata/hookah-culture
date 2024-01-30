"""
This module contains functions related to handling 
contact messages through a form.
"""
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    """
    Handles user messages submitted through a contact form.
    Processes form submissions, sends confirmation emails, 
    and displays success messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # Confirmation email is sent on submission of the form
            topic = form.cleaned_data['topic']
            name = form.cleaned_data['name']
            original_message = form.cleaned_data['message']
            message = render_to_string(
                'contact/confirmation_email/confirmation_email.txt', {
                    'name': name,
                    'original_message': original_message
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                topic,
                message,
                email_from,
                email_to
            )

            messages.success(request, 'Message submitted successfully! \
                A confirmation email is sent with the original message')

            # Redirect to the success page
            return HttpResponseRedirect(reverse('contact_success'))

    else:
        form = ContactForm()  # Create an instance of the form

    context = {
        'form': form,
    }

    template = 'contact/contact.html'

    return render(request, template, context)


def contact_success(request):
    """
    Renders the HTML page for displaying a success message 
    after submitting the contact form.
    """

    return render(request, 'contact/contact_success.html')
