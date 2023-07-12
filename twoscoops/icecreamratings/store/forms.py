from django import forms
from .models import IceCreamStore

class IceCreamStoreUpdateForm(forms.ModelForm):
    class Meta:
        model = IceCreamStore

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = True
        self.fields['description'].required = True

    class Meta(IceCreamStoreCreateForm.Meta):
        fields = ['title', 'block_address', 'phone', 'description']