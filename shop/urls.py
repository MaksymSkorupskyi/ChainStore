from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, reverse_lazy
from shop.views import ShopList, CustomShopDetailView, ShopEdit, ShopDelete, ShopCreate, ShopUpdate
from shop.views import ShopTypeList, CustomShopTypeDetailView, ShopTypeEdit, ShopTypeDelete, test

urlpatterns = [

    # Shops
    path('shop/', login_required(ShopList.as_view()), name='shop'),
    re_path(r'^shop/(?P<pk>\d+)/$', login_required(CustomShopDetailView.as_view()), name='shop'),
    # re_path(r'^shop/(?P<pk>\d+)/$', ShopDetail.as_view(), name='shop'),
    # re_path(r'^shop/add$', ShopCreate.as_view(), name='shop_add'),
    re_path(r'^shop/(?P<pk>\d+|new)/edit$', login_required(ShopEdit.as_view()), name='shop_edit'),
    re_path(r'^shop/(?P<pk>\d+)/delete$', login_required(ShopDelete.as_view()), name='shop_delete'),

    # Shop Types
    path('shoptype/', ShopTypeList.as_view(), name='shoptype'),
    re_path(r'^shoptype/(?P<pk>\d+)/$', CustomShopTypeDetailView.as_view(), name='shoptype'),
    # re_path(r'^shoptype/(?P<pk>\d+)/$', ShopTypeDetail.as_view(), name='shoptype'),
    re_path(r'^shoptype/(?P<pk>\d+|new)/edit$', login_required(ShopTypeEdit.as_view()), name='shoptype_edit'),
    re_path(r'^shoptype/(?P<pk>\d+)/delete$', login_required(ShopTypeDelete.as_view()), name='shoptype_delete'),

    path('shop/test', test),
]
