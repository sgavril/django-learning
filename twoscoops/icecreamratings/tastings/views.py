from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, UpdateView

from .models import Tasting, Taster
from .forms import TasterForm


class TasteListView(ListView):
    model = Tasting

class TasteDetailView(DetailView):
    model = Tasting

class TasteResultsView(TasteDetailView):
    template_name = 'tastings/results.html'

class TasteUpdateView(UpdateView):
    model = Tasting

def get_success_url(self):
    return reverse('tastings:detail', kwargs={'pk': self.object.pk})

class TasterUpdateView(LoginRequiredMixin, UpdateView):
    model = Taster
    form_class = TasterForm
    success_url = 'taster_success'

    def get_form_kwargs(self):
        """ This method is what injects forms with keyword arguments."""
        # Grab the current set of form #kwargs
        kwargs = super().get_form_kwargs()
        # Update kwargs with user_id
        kwargs['user'] = self.request.user
        return kwargs