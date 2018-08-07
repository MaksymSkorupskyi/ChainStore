from django.contrib import admin
from warehouse.models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'address',
        'id',
    )
    list_display_links = (
        'name',
        'city',
        'address',
        'id',
    )
    list_editable = (
        # 'name',
        # 'city',
        # 'address',
        # 'id',
    )
    list_filter = (
        'city',
    )


admin.site.register(Warehouse, WarehouseAdmin)
