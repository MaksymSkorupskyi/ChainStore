from django.contrib import admin
from shop.models import ShopType
from shop.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'shop_type',
        'owner',
        'city',
        'address',
        'website',
        'id',
    )
    list_display_links = (
        'name',
        'shop_type',
        # 'owner',
        'city',
        'address',
        'website',
        'id',
    )
    list_editable = (
        # 'name',
        # 'shop_type',
        'owner',
        # 'city',
        # 'address',
        # 'website',
    )
    list_filter = (
        'shop_type',
        'owner',
    )


admin.site.register(ShopType)
admin.site.register(Shop, ShopAdmin)
