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

class IceCreamOrderForm(forms.Form):
    slug = forms.ChoiceField(label='Flavor')
    toppings = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].choices = [
            (x.slug, x.title) for x in Flavor.objects.all()
        ]

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Flavor.objects.get(slug=slug).scoops_remaining <= 0:
            msg = 'Sorry, we are out of that flavor.'
            raise forms.ValidationError(msg)
        return slug

    def clean(self):
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug', '')
        toppings = cleaned_data.get('toppings', '')

        # Too much chocolate validation example
        in_slug = 'chocolate' in slug.lower()
        in_toppings = 'chocolate' in toppings.lower()
        if in_slug and in_toppings:
            msg = 'Your order has too much chocolate.'
            raise forms.ValidationError(msg)
        return cleaned_data