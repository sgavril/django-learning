from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import Flavour
from store.exceptions import OutOfStock, CorruptedDatabase

def list_flavor_line_item(sku):
    """
    Retrieve a Flavor object with specified SKU and non-zero quantity.
    """
    try:
        return Flavour.objects.get(sku=sku, quantity__gt=0)
    except Flavour.DoesNotExist: # exception for a specific model 
        msg = 'We are out of {0}'.format(sku)
        raise OutOfStock(msg)
    
def list_any_line_item(model, sku):
    """
    Retrieve 
    """
    try:
        return Flavour.objects.get(sku=sku, quantity__gt=0)
    except ObjectDoesNotExist: # exception for any model object
        msg = 'We are out of {0}'.format(sku)
        raise OutOfStock(msg)

def list_flavour_line_item(sku):
    try:
        Flavour.objects.get(sku=sku, quantity__gt=0)
    except Flavour.MultipleObjectsReturned:
        msg = 'Multiple objects have SKU {}. Please fix!'.format(sku)
        raise CorruptedDatabase(msg)