from django.contrib import admin
from person.models import Person
from shop.models import Shop


class OwnerShopInline(admin.TabularInline):
    # class OwnerShopInline(admin.StackedInline):
    model = Shop
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    inlines = (OwnerShopInline,)
    list_display = (
        # '__str__',
        'first_name',
        'last_name',
        'birthdate',
        'gender',
        'email',)


admin.site.register(Person, PersonAdmin)
