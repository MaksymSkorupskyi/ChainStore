from django.db import models
from Person.models import Person
from Warehouse.models import Warehouse
from Place.models import City


class ShopType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Shop(models.Model):
    shop_type = models.ForeignKey(ShopType, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Person, related_name='shop_owner', on_delete=models.PROTECT)
    sellers = models.ManyToManyField(Person, related_name='sellers')
    warehouses = models.ManyToManyField(Warehouse)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    address = models.CharField(max_length=250)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.shop_type} ({self.city})'
