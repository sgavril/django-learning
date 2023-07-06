from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.functional import cached_property
from django.views.generic import CreateView, UpdateView, TemplateView

from .models import Flavour
from .mixins import FreshFruitMixin, FavoriteMixin
from .tasks import update_user_who_favorited

class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ['title', 'slug', 'scoops_remaining']

    def form_valid(self, form):
        # Custom logic here
        return super().form_valid(form)

    def form_invlaid(self, form):
        # Custom logic here
        return super().form_invalid(form)

class FlavorUpdateView(LoginRequiredMixin,
                       FavoriteMixin,
                       UpdateView):
    model = Flavor
    fields = ['title', 'slug', 'scoops_remaining']

    def form_valid(self, form):
        update_user_who_favorited(
            instance=self.object,
            favorites=self.likes_and_favorites['favorites']
        )
        return super().form_valid(form)

class FlavorDetailView(LoginRequiredMixin,
                       FavoriteMixin,
                       TemplateView):
    model = Flavor

class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = "fruity_flavour.html"