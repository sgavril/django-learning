from django import forms

from .models import Taster

class TasterForm(forms.ModelForm):
    class Meta:
        model = Taster

    def __init__(self, *args, **kwargs):
        # Set the user as an attribute of the form
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
