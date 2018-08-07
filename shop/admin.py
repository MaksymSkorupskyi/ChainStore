from django.contrib import admin
from shop.models import ShopType
from shop.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        # '__str__',
        'name',
        'shop_type',
        'owner',
        # 'city.country',
        'city',
        'address',
        'website',
    )


admin.site.register(ShopType)
admin.site.register(Shop, ShopAdmin)
