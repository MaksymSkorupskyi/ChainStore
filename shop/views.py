from datetime import datetime

from django.contrib import messages
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView

from shop.forms import ShopForm, ShopTypeForm
from shop.models import Shop, ShopType
from person.models import Person
from warehouse.models import Warehouse

# __ Shop views _________________________________________________________________
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
    # model = Shop
    queryset = Shop.objects.select_related('shop_type', 'owner', 'city', 'city__country')
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
"""


class ShopDetail(DetailView):
    queryset = Shop.objects.select_related(
        'shop_type', 'owner', 'city', 'city__country',
    ).prefetch_related(
        Prefetch('sellers', Person.objects.order_by()),
        Prefetch('warehouses', Warehouse.objects.select_related('city', 'city__country'))
    )
    # model = Shop
    context_object_name = 'shop'
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shops'
        return context


class CustomShopDetailView(TemplateView):
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = get_object_or_404(Shop, pk=kwargs['pk'])
        context['main_menu_key'] = 'shops'
        return context


class ShopEdit(TemplateView):
    template_name = 'shop/shop_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if kwargs['pk'] != 'new':
            self.instance = get_object_or_404(Shop, pk=kwargs['pk'])
        else:
            self.instance = None
        self.form = ShopForm(request.POST or None, instance=self.instance)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shops'
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            saved_instance = self.form.save()
            if not self.instance:
                messages.success(request, 'Successfully created!')
            else:
                messages.success(request, 'Successfully saved!')
            return redirect('shop_edit', pk=saved_instance.pk)
        return self.get(request, *args, **kwargs)


class ShopUpdate(UpdateView):
    model = Shop
    fields = ('name', 'shop_type', 'owner', 'address', 'city', 'sellers', 'warehouses', 'website')
    # template_name = 'shop/shop_edit.html'


class ShopCreate(CreateView):
    model = Shop
    fields = ('name', 'shop_type', 'owner', 'address', 'city', 'sellers', 'warehouses', 'website')


class ShopDelete(DeleteView):
    model = Shop
    success_url = reverse_lazy('shop')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shops'
        return context


# __ ShopType views _________________________________________________________________
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


class ShopTypeEdit(TemplateView):
    template_name = 'shop/shoptype_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if kwargs['pk'] != 'new':
            self.instance = get_object_or_404(ShopType, pk=kwargs['pk'])
        else:
            self.instance = None
        self.form = ShopTypeForm(request.POST or None, instance=self.instance)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shoptypes'
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            saved_instance = self.form.save()
            if not self.instance:
                messages.success(request, 'Successfully created!')
            else:
                messages.success(request, 'Successfully saved!')
            return redirect('shoptype_edit', pk=saved_instance.pk)
        return self.get(request, *args, **kwargs)


class ShopTypeDelete(DeleteView):
    model = ShopType
    success_url = reverse_lazy('shoptype')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'shoptypes'
        return context


# __ experiments ____________________________________________________________________
def test(request):
    return render(request, 'shop/test/test.html', {
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
