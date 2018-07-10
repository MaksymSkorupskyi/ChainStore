from django.urls import path, re_path
from shop.views import ShopList, ShopDetail, ShopTypeList, ShopTypeDetail

urlpatterns = [
    path('shop/', ShopList.as_view(), name='shop'),
    re_path(r'^shop/(?P<pk>\d+)/$', ShopDetail.as_view(), name='shop'),
    path('shoptype/', ShopTypeList.as_view(), name='shoptype'),
    re_path(r'^shoptype/(?P<pk>\d+)/$', ShopTypeDetail.as_view(), name='shoptype'),
]