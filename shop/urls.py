from django.urls import path, re_path, reverse_lazy
from shop.views import ShopList, ShopCreate, ShopDelete, ShopUpdate, CustomShopDetailView
from shop.views import ShopTypeList, CustomShopTypeDetailView

urlpatterns = [
    path('shop/', ShopList.as_view(), name='shop'),
    # re_path(r'^shop/(?P<pk>\d+)/$', ShopDetail.as_view(), name='shop'),
    re_path(r'^shop/(?P<pk>\d+)/$', CustomShopDetailView.as_view(), name='shop'),
    re_path(r'^shop/add$', ShopCreate.as_view(), name='shop_add'),
    re_path(r'^shop/(?P<pk>\d+)/edit$', ShopUpdate.as_view(), name='shop_edit'),
    re_path(r'^shop/(?P<pk>\d+)/delete$', ShopDelete.as_view(), name='shop_delete'),

    path('shoptype/', ShopTypeList.as_view(), name='shoptype'),

    re_path(r'^shoptype/(?P<pk>\d+)/$', CustomShopTypeDetailView.as_view(), name='shoptype'),
    # re_path(r'^shoptype/(?P<pk>\d+)/$', ShopTypeDetail.as_view(), name='shoptype'),
]
