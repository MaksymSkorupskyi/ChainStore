from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from warehouse.forms import WarehouseForm
from warehouse.models import Warehouse

"""
def warehouse_list(request):
    return render(request, 'warehouse_list.html', {
        'warehouses': Warehouse.objects.all(),
        'main_menu_key': 'warehouses',
    })
"""


class WarehouseList(ListView):
    queryset = Warehouse.objects.select_related('city', 'city__country')
    # model = Warehouse
    context_object_name = 'warehouses'
    template_name = 'warehouse/warehouse_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'warehouses'
        return context


"""
def warehouse_detail(request, pk):
    return render(request, 'warehouse_detail.html', {
        'warehouse': get_object_or_404(Warehouse, pk=pk),
        'main_menu_key': 'warehouses',
    })
"""


class WarehouseDetail(DetailView):
    queryset = Warehouse.objects.select_related('city', 'city__country')
    # model = Warehouse
    context_object_name = 'warehouse'
    template_name = 'warehouse/warehouse_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'warehouses'
        return context


class WarehouseDelete(PermissionRequiredMixin, DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouse')
    permission_required = 'warehouse.delete_warehouse'

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'warehouses'
        return context


# @login_required
@permission_required('warehouse.add_warehouse')
def warehouse_edit(request, pk):
    if pk == 'new':
        instance = None
    else:
        instance = get_object_or_404(Warehouse, pk=pk)
    form = WarehouseForm(request.POST or None, instance=instance)
    if form.is_valid():
        warehouse = form.save()
        messages.success(request, 'Successfully saved!')
        return redirect('warehouse_edit', pk=warehouse.pk)
    return render(
        request,
        'warehouse/warehouse_edit.html',
        {
            'main_menu_key': 'warehouses',
            'form': form,
        },
    )
