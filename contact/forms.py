"""
This module contains the ContactForm class, 
which is a ModelForm for the Contact model.
"""
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    This class is a ModelForm for the Contact model. 
    It specifies the fields to be included in
    the form and customizes their appearance, 
    including setting placeholders and adding classes.
    """
    class Meta:
        """
        This class defines metadata options for the form, 
        specifying the model and fields to include.
        """
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        This method customizes the form's appearance, 
        including setting placeholders,
        removing the 'status' field, and adding classes to fields.
        """
        super().__init__(*args, **kwargs)

        self.fields.pop('status', None)

        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'message': 'Your Message',
        }

        for field in self.fields:
            if field != 'topic':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'my-2'

                if field == 'message' and isinstance(self.fields[field].widget, forms.Textarea):
                    self.fields[field].widget.attrs['rows'] = 6

            self.fields[field].label = False
