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
        'first_name',
        'last_name',
        'birthdate',
        'gender',
        'email',
        'id',
    )
    list_display_links = (
        'first_name',
        'last_name',
        'birthdate',
        # 'gender',
        'email',
        'id',
    )
    list_editable = (
        # 'first_name',
        # 'last_name',
        # 'birthdate',
        'gender',
        # 'email',
        # 'id',
    )
    list_filter = (
        'gender',
    )


admin.site.register(Person, PersonAdmin)
