from django.db import models
from person.models import Person
from warehouse.models import Warehouse
from place.models import City


class ShopType(models.Model):
    name = models.CharField(max_length=50, verbose_name='shop type', unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Shop(models.Model):
    shop_type = models.ForeignKey(ShopType, verbose_name='shop type', on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name='name')
    owner = models.ForeignKey(Person, verbose_name='shop owner', related_name='shop_owner', on_delete=models.PROTECT)
    sellers = models.ManyToManyField(Person, verbose_name='sellers', related_name='sellers')
    warehouses = models.ManyToManyField(Warehouse, verbose_name='warehouses')
    city = models.ForeignKey(City, verbose_name='city', on_delete=models.PROTECT)
    address = models.CharField(max_length=250, verbose_name='address', blank=True)
    website = models.URLField(verbose_name='web site', blank=True)

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.shop_type} | {self.city}'
