from datetime import datetime
from django.utils import timezone
from django.utils.html import mark_safe
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView

from shop.models import Shop, ShopType

# Shop views
"""
def shop_list(request):
    return render(
        request,
        'shop_list.html',
        {
            'shops': Shop.objects.all(),
            'main_menu_key': 'shops',
        },
    )
"""


class ShopList(ListView):
    model = Shop
    context_object_name = 'shops'
    template_name = 'shop/shop_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shops'
        return context


"""
def shop_detail(request, pk):
    return render(request, 'shop_detail.html', {
        'shop': get_object_or_404(Shop, pk=pk),
        'main_menu_key': 'shops',
    })


class ShopDetail(DetailView):
    model = Shop
    context_object_name = 'shop'
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shops'
        return context
"""


class CustomShopDetailView(TemplateView):
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = get_object_or_404(Shop, pk=kwargs['pk'])
        context['main_menu_key'] = 'shops'
        return context


class ShopUpdate(UpdateView):
    model = Shop
    fields = ('name', 'shop_type', 'owner', 'address', 'city', 'sellers', 'warehouses', 'website')
    # context_object_name = 'shop_edit'
    # template_name = 'shop/shop_form.html'


class ShopCreate(CreateView):
    model = Shop
    fields = ('name', 'shop_type', 'owner', 'address', 'city', 'sellers', 'warehouses', 'website')


class ShopDelete(DeleteView):
    model = Shop
    success_url = "/shop"


# ShopType views
"""
def shoptype_list(request):
    return render(request, 'shoptype_list.html', {
        'shoptypes': ShopType.objects.all(),
        'main_menu_key': 'shoptypes',
    })
"""


class ShopTypeList(ListView):
    model = ShopType
    context_object_name = 'shoptypes'
    template_name = 'shop/shoptype_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shoptypes'
        return context


"""
def shoptype_detail(request, pk):
    return render(request, 'shoptype_detail.html', {
        'shoptype': get_object_or_404(Shoptype, pk=pk),
        'main_menu_key': 'shoptypes',
    })


class ShopTypeDetail(DetailView):
    model = ShopType
    context_object_name = 'shoptype'
    template_name = 'shop/shoptype_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shoptypes'
        return context
"""


class CustomShopTypeDetailView(TemplateView):
    template_name = 'shop/shoptype_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoptype'] = get_object_or_404(ShopType, pk=kwargs['pk'])
        context['main_menu_key'] = 'shoptypes'
        return context


# experiments
def test(request):
    return render(request, 'shop/test.html', {
        'a': '<b>hello</b>',
        'b': ['<b>hello</b>', '<i>world</i>', ],
        'd': {'a': 1, 'b': {'z': 4}, 'c': 3},
        'obj': Shop.objects.first(),
        'x': 4,
        'r': range(20),
        't0': '',
        't1': 'Hello',
        't2': 'World',
        'items': Shop.objects.all(),
        'items2': [
            {'name': 'Aaa', 'n': 1},
            {'name': 'Aaa', 'n': 2},
            {'name': 'Bbb', 'n': 3},
        ],
        'y': 5,
        'list1': [1, 2],
        'list2': [3, 4],
        'yy': "'hello'",
        'zz': 'hello',
        'xx': datetime.now(),
        'aa': 'Hello Person!',
        'bb': 123213423542,
        'cc': 1.28,
        'dd': '?q=поиск',
        'ee': (
            'Text Текст\n'
            'text текст\n\n'
            'New Paragraph'
        ),
        'ff': datetime(2013, 1, 1),
        'gg': datetime(2019, 1, 1),
        't': '<b>very</b> interesting page' * 100,
        'test': '<b> t e s t </b>',
        'time_now': timezone.now(),
        'date_prefix': 'Date: ',
        'selected_menu': 0,
    })
