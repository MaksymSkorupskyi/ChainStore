from django import forms
from shop.models import Shop, ShopType


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopTypeForm(forms.ModelForm):
    class Meta:
        model = ShopType
        fields = '__all__'