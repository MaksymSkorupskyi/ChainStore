from django.urls import path, re_path

from warehouse.views import WarehouseList, WarehouseDetail, WarehouseDelete, warehouse_edit

urlpatterns = [
    path('warehouse/', WarehouseList.as_view(), name='warehouse'),
    re_path(r'^warehouse/(?P<pk>\d+)/$', WarehouseDetail.as_view(), name='warehouse'),

    path('warehouse/add', warehouse_edit, name='warehouse_edit'),
    re_path(r'^warehouse/(?P<pk>\d+|new|add)/edit$', warehouse_edit, name='warehouse_edit'),

    re_path(r'^warehouse/(?P<pk>\d+)/delete$', WarehouseDelete.as_view(), name='warehouse_delete'),
]
