"""
This module defines a Django form class
`ReviewForm` for handling user reviews.
It utilizes the Review model from the same
app and includes fields for title, content,
and rating. The rating field is presented as
a radio button set.
"""
from django import forms
from .models import Review

RATINGS = [(1, 'Very poor'),
            (2, 'Poor'),
            (3, 'Ok'),
            (4, 'Good'),
            (5, 'Excellent')]

class ReviewForm(forms.ModelForm):
    """
    Django form class for handling reviews.
    """
    class Meta:
        """
        Meta class for ReviewForm.
        This class defines metadata options
        for the ReviewForm, specifying the model
        it is associated with (Review) and
        the fields it includes.
        """
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(
        label='How will you rate this product?',
        choices=RATINGS,
        widget=forms.RadioSelect(attrs={'class': 'rating-radio'})
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the ReviewForm.
        This method sets up additional
        attributes and styling for the form.
        """
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['rows'] = 2
        self.fields['content'].widget.attrs['style'] = 'margin-top: 10px;'

        placeholders = {
            'title': 'Title',
            'content': 'Content',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'textarea form-control'

            if field_name == 'rating':
                self.fields[field_name].label = 'How will you rate this product?'
            else:
                self.fields[field_name].label = False

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

        self.fields['title'].widget.attrs['autofocus'] = True
