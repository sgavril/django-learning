from django.shortcuts import render, get_object_or404
from django.http import HttpRequest, HttpResponse

from .decorators import check_sprinkles
from .models import Sprinkle
from .utils import check_sprinkle_rights


def sprinkle_list(request: HttpRequest) -> HttpResponse:
    """Standard list view"""
    request = check_sprinkles(request)

    return render(request,
        "sprinkles/sprinkle_list.html",
        {"sprinkles": Sprinkle.objects.all()})

@check_sprinkles
def sprinkle_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Standard detail view."""
    request = check_sprinkles(request)

    sprinkle = get_object_or404(Sprinkle, pk=pk)

    return render(request, "sprinkles/sprinkle_detail.html",
        {"sprinkle": sprinkle})

def sprinkle_preview(request: HttpRequest) -> HttpResponse:
    """ Preview of new sprinkle, but without check_sprinkles """
    sprinkle = Sprinkle.objects.all()
    return render(request,
        "sprinkles/sprinkle_preview.html",
        {"sprinkle": sprinkle})

class SprinkleDetail(DetailView):
    """ Standard detail view. """
    model = Sprinkle

    def dispatch(self, request, *args, **kwargs):
        request = check_sprinkles(request)
        return super().dispatch(request, *args, **kwargs)

