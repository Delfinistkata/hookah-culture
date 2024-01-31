from django import forms
from .models import Review

RATINGS = [(1, 'Very bad'),
            (2, 'Bad'),
            (3, 'Ok'),
            (4, 'Good'),
            (5, 'Great!')]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')

    rating = forms.ChoiceField(
        label='How will you rate this product?',
        choices=RATINGS,
        widget=forms.RadioSelect(attrs={'class': 'rating-radio'})
    )

    def __init__(self, *args, **kwargs):
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
