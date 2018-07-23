from django import forms
from warehouse.models import Warehouse


class WarehouseForm(forms.ModelForm):
    # name = forms.CharField(
    #     # label='Warehouse Name',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-group',
    #             'placeholder': 'Warehouse name'
    #         },
    #     ))
    # city = forms.ChoiceField(
    #     widget=forms.ChoiceField(
    #         attrs={
    #             'class': 'form-group',
    #             'placeholder': 'Choose city...',
    #         },
    #     ),
    # )

    class Meta:
        model = Warehouse
        fields = '__all__'
