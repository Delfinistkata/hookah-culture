"""
Forms for User Profile Management.
This module defines forms related to user profile management, including the
UserProfileForm used for updating user profile information.
"""
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.
    This form extends the built-in ModelForm and is specifically designed
    for updating the user profile information. It excludes the 'user' field
    as it is automatically associated with the logged-in user.
    """
    class Meta:
        """
        Metadata class for UserProfileForm.
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'shadow-lg p-2 bg-body-tertiary rounded mb-2 '
                'profile-form-input'
            )
            self.fields[field].label = False
