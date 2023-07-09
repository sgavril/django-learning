from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.functional import cached_property
from django.views.generic import CreateView, UpdateView, TemplateView, ListView

from .models import Flavor
from .mixins import FreshFruitMixin, FavoriteMixin, FlavorActionMixin
from .tasks import update_user_who_favorited

class FlavorCreateView(LoginRequiredMixin,
                       FlavorActionMixin,
                       CreateView):
    model = Flavor
    success_msg = "Flavor created!"

class FlavorUpdateView(LoginRequiredMixin,
                       FlavorActionMixin(),
                       UpdateView):
    model = Flavor
    success_msg = "Flavor updated!"

class FlavorDetailView(LoginRequiredMixin,
                       FavoriteMixin,
                       TemplateView):
    model = Flavor

class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = "fruity_flavour.html"

class FlavorListView(ListView):
    model = Flavor

    def get_queryset(self):
        # Fetch queryset from parent
        queryset = super().get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)

        return queryset