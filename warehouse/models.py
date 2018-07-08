from django.db import models
from place.models import City


class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    address = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'warehouse'
        verbose_name_plural = 'warehouses'
        ordering = ('name', 'city')

    def __str__(self):
        return f'{self.name} | {self.city}'
