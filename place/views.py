# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from place.models import Country, City

# Country
"""
def country_list(request):
    return render(request, 'place/country_list.html', {
        'countries': Country.objects.all(),
        'main_menu_key': 'countries',
    })
"""


class CountryList(ListView):
    model = Country
    context_object_name = 'countries'
    template_name = 'place/country_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'countries'
        return context


"""
def country_detail(request, pk):
    return render(request, 'place/country_detail.html', {
        'country': get_object_or_404(Country, pk=pk),
        'main_menu_key': 'countries',
    })
"""


class CountryDetail(DetailView):
    model = Country
    context_object_name = 'country'
    template_name = 'place/country_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'countries'
        return context


# City
"""
def city_list(request):
    return render(request, 'place/city_list.html', {
        'cities': City.objects.select_related('country'),
        'main_menu_key': 'cities',
    })
"""


class CityList(ListView):
    queryset = City.objects.select_related('country')
    context_object_name = 'cities'
    template_name = 'place/city_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'cities'
        return context


"""
def city_detail(request, pk):
    return render(request, 'place/city_detail.html', {
        'city': get_object_or_404(City.objects.select_related('country'), pk=pk),
        'main_menu_key': 'cities',
    })
"""


class CityDetail(DetailView):
    queryset = City.objects.select_related('country')
    context_object_name = 'city'
    template_name = 'place/city_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'cities'
        return context
