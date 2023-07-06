from django.db import models
from django.urls import reverse
from core.models import TimeStampedModel

class Flavour(TimeStampedModel):
    title = models.CharField(max_length=200)

class Flavor(models.Model):
    class Scoops(models.IntegerChoices):
        SCOOPS_0 = 0
        SCOOPS_1 = 1

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(choices=Scoops.choices,
        default=Scoops.SCOOPS_0)

    def get_absolute_url(self):
        return reverse("flavours:detail", kwargs={"slug": self.slug})