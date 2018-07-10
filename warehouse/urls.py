from django.urls import path, re_path
from warehouse.views import WarehouseList, WarehouseDetail

urlpatterns = [
    path('warehouse/', WarehouseList.as_view(), name='warehouse'),
    re_path(r'^warehouse/(?P<pk>\d+)/$', WarehouseDetail.as_view(), name='warehouse'),
]