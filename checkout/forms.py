"""
Django form for the Order model.
It is is used to collect and validate user
input for creating or updating
an order. It inherits from Django's ModelForm
and customizes the appearance
of the form fields by setting placeholders,
classes, and removing auto-generated labels.
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for collecting and validating user input for orders.
    It captures information related to an order,
    such as customer details and shipping information.
    """
    class Meta:
        """
        Inner class defining metadata options for the OrderForm.
        The Meta class specifies metadata options for the OrderForm,
        including the associated model and
        the fields to be included in the form.
        These options influence the behavior
        and appearance of the form when rendered.
        """
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode',
            'country', 'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address',
            'street_address2': 'Street Address',
            'postcode': 'Postal Code',
            'town_or_city': 'City',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'stripe-style-input mt-1 mb-1'
            )
            self.fields[field].label = False
