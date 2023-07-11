from django.db import models

from .validators import validate_tasty

class TastyTitleAbstractModel(models.Model):
    title = models.CharField(max_length=255, validators=[validate_tasty])

    class Meta:
        abstract = True

class TimeStampedModel(models.Model):
    """
    Abstract base class model providing self-updating
    fields for `created` and `modified`.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True