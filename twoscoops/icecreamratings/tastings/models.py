from django.db import models
from core.models import TimeStampedModel


class Taster(models.Model):
    name = models.CharField(max_length=200)

class Tasting(TimeStampedModel):
    title = models.CharField(max_length=200)