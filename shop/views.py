from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from shop.models import Shop, ShopType


def shop_list(request):
    return render(request, 'shop_list.html', {
        'shops': Shop.objects.all(),
        'main_menu_key': 'shops',
    })


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


def shoptype_list(request):
    return render(request, 'shoptype_list.html', {
        'shoptypes': ShopType.objects.all(),
        'main_menu_key': 'shoptypes',
    })


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
        return context
