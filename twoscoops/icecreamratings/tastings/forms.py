from django import forms

from .models import Taster, Tasting

class TasterForm(forms.Form):
    class Meta:
        model = Taster

    def __init__(self, *args, **kwargs):
        # Set the user as an attribute of the form
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

class IceCreamReviewForm(forms.Form):
    class Meta:
        model = Tasting

    fields = ['flavor', 'age']

    def clean(self):
        cleaned_data = super().clean()
        flavor = cleaned_data.get('flavor')
        age = cleaned_data.get('age')

        if flavor == 'coffee' and age < 3:
            # Record errors here
            msg = 'Coffee ice cream is not for babies.'
            self.add_error('flavor', msg)
            self.add_error('age', msg)

        return cleaned_data