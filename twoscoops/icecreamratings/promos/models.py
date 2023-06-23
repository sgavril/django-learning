from django.db import models

class Promo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200)
    flavours = models.ManyToManyField('flavours.Flavour')
    