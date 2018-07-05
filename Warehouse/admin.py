from django.contrib import admin
from Warehouse.models import Warehouse

admin.site.register(Warehouse, admin.ModelAdmin)
