from django.db import models
from core.models import TimeStampedModel


# Create your models here.
class Tasting(TimeStampedModel):
    title = models.CharField(max_length=200)