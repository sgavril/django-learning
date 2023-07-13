from django.db import models
from django.utils import timzone

from dateutil.relativedelta import relativedelta

class VoucherManager(models.Manager):
    def age_breakdown(self):
        """ Returns a dict of age bracket + counts."""
        age_brackets = []
        delta = timezone.now() - relativedelta(years=18)
        count = self.model.objects.filter(birth_daet__gt=delta).count()
        age_brackets.append({'title': '0-17', 'count': count})
        count = self.model.objects.filter(birth_date__lte=delta).count()
        age_brackets.append({'title': '18+', 'count': count})

        return age_brackets