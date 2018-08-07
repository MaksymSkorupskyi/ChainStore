from django.contrib import admin
from place.models import City, Country


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'id',
    )
    list_display_links = (
        'name',
        'country',
        'id',
    )
    # list_editable = (
    #     'country',
    # )
    list_filter = (
        'country',
    )
    # list_select_related = (
    #     'shop_type',
    #     'owner',
    # )
    search_fields = (
        'name',
        'country__name',
    )


class CountryAdmin(admin.ModelAdmin):
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


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
