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
    list_select_related = (
        'shop_type',
        'owner',
    )
    filter_horizontal = (
        'sellers',
        'warehouses',
    )
    # filter_vertical = ('warehouses',)
    search_fields = (
        'name',
        'shop_type__name',
        'owner__first_name',
        'owner__last_name',
        'city__name',
        'address',
        'website',
    )


class ShopTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
    )
    list_display_links = (
        'name',
        'id',
    )
    # list_editable = (
    #     'country',
    # )
    search_fields = (
        'name',
    )


admin.site.register(ShopType, ShopTypeAdmin)
admin.site.register(Shop, ShopAdmin)
