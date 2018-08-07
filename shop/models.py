from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from django.urls import reverse

from person.models import Person
from warehouse.models import Warehouse
from place.models import City
from django.utils.translation import ugettext_lazy as _


class ShopType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    shop_type = models.ForeignKey(ShopType, verbose_name=_('type'), on_delete=models.PROTECT)
    owner = models.ForeignKey(Person, verbose_name=_('owner'), related_name='shop_owner', on_delete=models.PROTECT)
    address = models.CharField(max_length=250, verbose_name=_('address'), blank=True)
    city = models.ForeignKey(City, verbose_name=_('city'), on_delete=models.PROTECT)
    website = models.URLField(verbose_name=_('website'), blank=True)
    sellers = models.ManyToManyField(Person, verbose_name=_('sellers'), related_name='sellers')
    warehouses = models.ManyToManyField(Warehouse, verbose_name=_('warehouses'))
    version = models.PositiveIntegerField(verbose_name=_('version'), default=0, editable=False)

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.shop_type} | {self.city}'

    def get_absolute_url(self):
        return reverse('shop', kwargs={'pk': self.pk})


"""
    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'pk': self.pk})

    @models.permalink
    def get_absolute_url(self):
        return 'shop', (), {'pk': self.pk}
"""


@receiver(post_save, sender=Shop)
def inc_shop_version(sender, instance, **kwargs):
    Shop.objects.filter(pk=instance.pk).update(version=F('version') + 1)
