"""
Newsletters Forms:
This module contains the form definitions for the 'newsletters' app.
Forms:
- SubscriberForm: Captures email addresses for newsletter subscriptions.
"""
from crispy_forms.helper import FormHelper

from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """
    Subscriber Form:
    This form is used for capturing email addresses from users who want to subscribe
    to newsletters. It extends Django's ModelForm and customizes its appearance
    using crispy_forms and additional field modifications.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with additional settings.
        This method sets up a FormHelper to customize the form's appearance,
        modifies the 'email' field label, and adds a placeholder to the
        'email' field.
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

    class Meta:
        """
        Meta class for the SubscriberForm.
        This class defines the model and fields for the form.
        """
        model = Subscriber
        fields = ('email',)
