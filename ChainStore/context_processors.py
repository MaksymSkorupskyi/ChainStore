# coding=utf-8
from django.urls import reverse_lazy

"""
MAIN_MENU = (
    ('shops', {'url': reverse_lazy('shop'), 'title': 'Shops'}),
    ('shop_types', {'url': reverse_lazy('shop_type'), 'title': 'Shop Types'}),
    ('persons', {'url': reverse_lazy('person'), 'title': 'Contact Persons'}),
    ('stocks', {'url': reverse_lazy('stock'), 'title': 'Warehouses'}),
    ('countries', {'url': reverse_lazy('country'), 'title': 'Countries'}),
    ('cities', {'url': reverse_lazy('city'), 'title': 'Cities'}),
)


def main(request):
    return {
        'DEFAULT_TITLE': 'ChainStore',
        'MAIN_MENU': MAIN_MENU,
    }
"""


def chainstore_constants(request):
    return {
        'AUTHOR': 'Maksym Skorupskyi',
        'WEBSITE': 'ChainStore',

        # 'data': get_data,

    }

# def get_data():
#     return [1, 2, 3]
