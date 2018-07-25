from django import forms
from place.models import City, Country


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
