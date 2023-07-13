from django.db import models

from .managers import VoucherManager

class Voucher(models.Model):
    """ Vouchers for free pints of ice cream. """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    birth_date = models.DateField(blank=True)
    sent = models.DateTimeField(null=True, default=None)
    redeemed = models.DateTimeField(null=True, default=None)
    objects = VoucherManager()