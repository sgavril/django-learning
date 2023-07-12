from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.functional import cached_property
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, ListView, View
from django.shortcuts import get_object_or_404, render, redirect

from core.views import TitleSearchMixin
from .forms import Flavor
from .models import Flavor
from .mixins import FreshFruitMixin, FavoriteMixin, FlavorActionMixin
from .tasks import update_user_who_favorited

class FlavorCreateView(LoginRequiredMixin,
                       FlavorActionMixin,
                       CreateView):
    success_msg = "Flavor created!"
    form_class = FlavorForm

class FlavorUpdateView(LoginRequiredMixin,
                       FlavorActionMixin,
                       UpdateView):
    success_msg = "Flavor updated!"
    form_class = FlavorForm

class FlavorDetailView(LoginRequiredMixin,
                       FavoriteMixin,
                       TemplateView):
    model = Flavor

class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = "fruity_flavour.html"

class FlavorListView(TitleSearchMixin, ListView):
    model = Flavor

def flavor_view(request):
    return render(request, 'flavours/base.html')

class FlavorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        flavor = get_object_or_404(Flavor, slug=kwargs['slug'])

        response = HttpResponse(content_type='application/pdf')
        response = make_flavor_pdf(response, flavor)

        return response

    def post(self, request, *args, **kwargs):
        flavor = get_object_or_404(Flavor, slug=kwargs['slug'])
        form = FlavorForm(request.POST, instance=flavor)
        if form.is_valid():
            form.save()
        return redirect("flavors:detail", flavor.slug)