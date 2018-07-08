from django.contrib import admin
from place.models import City, Country

admin.site.register((City, Country))
# admin.site.register(City, admin.ModelAdmin)
# admin.site.register(Country, admin.ModelAdmin)