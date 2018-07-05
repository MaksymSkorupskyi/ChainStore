from django.contrib import admin
from Shop.models import Shop
from Shop.models import ShopType

admin.site.register(ShopType, admin.ModelAdmin)
admin.site.register(Shop, admin.ModelAdmin)
