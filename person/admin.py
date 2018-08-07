from django.contrib import admin
from person.models import Person
from shop.models import Shop


class OwnerShopInline(admin.TabularInline):
    model = Shop


class PersonAdmin(admin.ModelAdmin):
    inlines = (OwnerShopInline, )


admin.site.register(Person, PersonAdmin)
