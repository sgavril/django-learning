from django.views.generic import TemplateView
import json
from django.contrib import messages
from django.core import serializers
from core.models import ModelFormFailureHistory

class FreshFruitMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_fresh_fruit'] = True
        return context

class FavoriteMixin:
    @cached_property
    def likes_and_favorites(self):
        """ Returns a dict of likes and favorites. """
        likes = self.object.likes()
        favourites = self.object.favorites()
        return {
            "likes": likes,
            "favorites": favorites,
            "favorites_count": favorites.count(),
        }

class FlavorActionMixin:

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)

    def form_invalid(self, form):
        """ Save invalid form and model data for later reference."""
        form_data = json.dumps(form.cleaned_data)
        # Serialize the instance
        model_data = serializers.serialize('json', [form.instance])
        # Strip awaay brackets leaving only a dict
        model_data = model_data[1:-1]
        ModelFormFailureHistory.objects.create(
            form_data=form_data,
            model_data=model_data
        )
        return super().form_invalid(form)