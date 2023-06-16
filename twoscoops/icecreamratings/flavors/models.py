from django.db import models
from core.models import TimeStampedModel

class Flavour(TimeStampedModel):
    title = models.CharField(max_length=200)