from django.shortcuts import render
from django.views.generic import ListView
from .forms import IceCreamStoreCreateForm, IceCreamStoreUpdateForm
from .models import IceCreamStore

class IceCreamStoreListView(TitleSearchMixin, ListView):
    model = Store

class IceCreamCreateView(CreateView):
    model = IceCreamStore
    form_class = IceCreamStoreCreateForm

class IceCreamUpdateView(UpdateView):
    model = IceCreamStore
    form_class = IceCreamStoreUpdateForm