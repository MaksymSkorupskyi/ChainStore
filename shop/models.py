from django.db import models
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

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.shop_type} | {self.city}'

    # def get_absolute_url(self):
    #     return reverse('shop_detail', kwargs={'pk': self.pk})

    # @models.permalink
    # def get_absolute_url(self):
    #     return 'shop', (), {'pk': self.pk}
