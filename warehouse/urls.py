from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from warehouse.views import WarehouseList, WarehouseDetail, WarehouseDelete, warehouse_edit

urlpatterns = [
    path('warehouse/', login_required(WarehouseList.as_view()), name='warehouse'),
    re_path(r'^warehouse/(?P<pk>\d+)/$', login_required(WarehouseDetail.as_view()), name='warehouse'),
    re_path(r'^warehouse/(?P<pk>\d+|new|add)/edit$', warehouse_edit, name='warehouse_edit'),
    re_path(r'^warehouse/(?P<pk>\d+)/delete$', login_required(WarehouseDelete.as_view()), name='warehouse_delete'),
]
