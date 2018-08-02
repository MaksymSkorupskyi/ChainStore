from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from place.forms import CountryForm, CityForm
from place.models import City, Country

# ___ Country views _________________________________________________________________
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


# @method_decorator(login_required, name='dispatch')
class CountryEdit(PermissionRequiredMixin, UpdateView):
    form_class = CountryForm
    model = Country
    template_name = 'place/country_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'countries'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Successfully saved!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('country_edit', kwargs={'pk': self.object.pk})


class CountryCreate(PermissionRequiredMixin, CreateView):
    form_class = CountryForm
    model = Country
    template_name = 'place/country_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'countries'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Successfully added!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('country_edit', kwargs={'pk': self.object.pk})


class CountryDelete(PermissionRequiredMixin, DeleteView):
    model = Country
    success_url = reverse_lazy('country')
    permission_required = 'country.delete_country'

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'countries'
        return context


# ___ City views _________________________________________________________________
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


class CityEdit(PermissionRequiredMixin, UpdateView):
    form_class = CityForm
    model = City
    template_name = 'place/city_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'cities'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Successfully saved!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('city_edit', kwargs={'pk': self.object.pk})


class CityCreate(PermissionRequiredMixin, CreateView):
    form_class = CityForm
    model = City
    template_name = 'place/city_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'countries'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Successfully added!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('city_edit', kwargs={'pk': self.object.pk})


class CityDelete(PermissionRequiredMixin, DeleteView):
    model = City
    success_url = reverse_lazy('city')
    permission_required = 'city.delete_city'

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'cities'
        return context
