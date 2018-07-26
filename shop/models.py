from django.db import models
from person.models import Person
from warehouse.models import Warehouse
from place.models import City


class ShopType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    shop_type = models.ForeignKey(ShopType, verbose_name='type', on_delete=models.PROTECT)
    owner = models.ForeignKey(Person, verbose_name='owner', related_name='shop_owner', on_delete=models.PROTECT)
    address = models.CharField(max_length=250, verbose_name='address', blank=True)
    city = models.ForeignKey(City, verbose_name='city', on_delete=models.PROTECT)
    website = models.URLField(verbose_name='website', blank=True)
    sellers = models.ManyToManyField(Person, verbose_name='sellers', related_name='sellers')
    warehouses = models.ManyToManyField(Warehouse, verbose_name='warehouses')

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.shop_type} | {self.city}'

    # def get_absolute_url(self):
    #     return reverse('shop_detail', kwargs={'pk': self.pk})

    @models.permalink
    def get_absolute_url(self):
        return 'shop', (), {'pk': self.pk}
