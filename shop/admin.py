from django.contrib import admin
from shop.models import ShopType
from shop.models import Shop

admin.site.register(ShopType)
admin.site.register(Shop)
# admin.site.register(ShopType, admin.ModelAdmin)
# admin.site.register(shop, admin.ModelAdmin)
