from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from warehouse.models import Warehouse


def warehouse_list(request):
    return render(request, 'warehouse_list.html', {
        'warehouses': Warehouse.objects.all(),
        'main_menu_key': 'warehouses',
    })


class WarehouseList(ListView):
    model = Warehouse
    context_object_name = 'warehouses'
    template_name = 'warehouse/warehouse_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'warehouses'
        return context


def warehouse_detail(request, pk):
    return render(request, 'warehouse_detail.html', {
        'warehouse': get_object_or_404(Warehouse, pk=pk),
        'main_menu_key': 'warehouses',
    })


class WarehouseDetail(DetailView):
    model = Warehouse
    context_object_name = 'warehouse'
    template_name = 'warehouse/warehouse_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'warehouses'
        return context
