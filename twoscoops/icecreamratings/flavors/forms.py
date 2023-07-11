from django import forms

from .models import Flavor
from core.validators import validate_tasty

class FlavorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].validators.append(validate_tasty)
        self.fields['slug'].validators.append(validate_tasty)

    class Meta:
        model = Flavor