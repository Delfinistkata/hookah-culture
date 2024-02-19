"""
Django form for the 'Product' model.
This form is used to handle the
input and validation for creating or
updating Product instances.
"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form class for handling Product model instances.
    """
    class Meta:
        """
        Metadata options for the ProductForm.
        This Meta class provides additional
        information about the behavior
        of the ProductForm, including the
        associated model and the fields
        to include in the form.
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Custom initialization method for the ProductForm.
        This method sets up form fields,
        placeholders, and widget attributes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'sku': 'Sku',
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image',
            'stock': 'Stock Amount',
        }

        self.fields['stock'] = forms.IntegerField(
            label='Stock Amount',
            widget=forms.NumberInput(attrs={'placeholder': 'Stock Amount'})
        )

        self.fields['description'].widget.attrs['rows'] = 2

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = (
                'shadow-lg p-2 bg-body-tertiary rounded mb-2'
            )

        self.fields['category'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'category':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'shadow-lg p-2 bg-body-tertiary rounded mb-2'
            )
            self.fields[field].label = False
