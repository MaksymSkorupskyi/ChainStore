from django.db import models
from place.models import City
from django.utils.translation import ugettext_lazy as _


class Warehouse(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    address = models.CharField(max_length=250, verbose_name=_('address'))
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name=_('city'))

    class Meta:
        verbose_name = _('warehouse')
        verbose_name_plural = _('warehouses')
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.city}'
