from django.db.models import Q

from .models import Promo

def fun_function(name=None):
    """ Find working icecream promo. """
    results = Promo.objects.active()
    results = results.filter(
        Q(name__startswith=name) |
        Q(description__icontains=name)
    )
    results = results.exclude(status='melted')
    results = results.select_related('flavours')
    return results