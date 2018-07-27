from django.urls import reverse_lazy
from datetime import datetime
from django.db import connection
from django.utils.translation import ugettext_lazy as _

MAIN_MENU = (
    ('shops', {'url': reverse_lazy('shop'), 'title': _('Shops')}),
    ('shoptypes', {'url': reverse_lazy('shoptype'), 'title': _('Shop Types')}),
    ('persons', {'url': reverse_lazy('person'), 'title': _('Persons')}),
    ('warehouses', {'url': reverse_lazy('warehouse'), 'title': _('Warehouses')}),
    ('cities', {'url': reverse_lazy('city'), 'title': _('Cities')}),
    ('countries', {'url': reverse_lazy('country'), 'title': _('Countries')}),
)


def copyright_year():
    opening_year = 2018
    current_year = datetime.now().year
    if current_year > opening_year:
        return f'{opening_year}-{current_year}'
    return opening_year


def chainstore_constants(request):
    return {
        'AUTHOR': 'Maksym Skorupskyi',
        'WEBSITE': 'ChainStore',
        'COPYRIGHT_YEAR': copyright_year(),
        'MAIN_MENU': MAIN_MENU,
        'sql_queries': connection.queries,
        # 'data': get_data,
    }

# def get_data():
#     return [1, 2, 3]
