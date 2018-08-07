from django.contrib import admin
from warehouse.models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'address',
    )


admin.site.register(Warehouse, WarehouseAdmin)
