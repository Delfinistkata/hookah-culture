from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    User can send message through the form
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Message submitted succesfully')

    form = ContactForm
    context = {
        'form': form
    }

    template = 'contact/contact.html'

    return render(request, template, context)
