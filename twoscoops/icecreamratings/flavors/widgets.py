from django.forms.widgets import TextInput

class IceCreamFlavorInput(TextInput):
    """Ice cream flavors must always end with 'Ice Cream'"""
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        value = context['widget']['value']
        if not value.strip().lower().endswith('ice cream'):
            context['widget']['value'] = '{} Ice Cream'.format(value)
        return context