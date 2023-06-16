from django.db import models

class TimeStampedModel(models.Model):
    """
    Abstract base class model providing self-updating 
    fields for `created` and `modified`.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True