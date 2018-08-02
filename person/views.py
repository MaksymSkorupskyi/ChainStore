from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from person.forms import PersonForm
from person.models import Person

"""
def person_list(request):
    return render(request, 'person/person_list.html', {
        'persons': Person.objects.all(),
        'main_menu_key': 'persons',
    })
"""


class PersonList(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'person/person_list.html'

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'persons'
        return context


"""
def person_detail(request, pk):
    return render(request, 'person_detail.html', {
        'person': get_object_or_404(Person, pk=pk),
        'main_menu_key': 'persons',
    })
"""


class PersonDetail(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'person/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'persons'
        return context


"""
# from django.http import Http404, HttpResponse
# from django.views.decorators.http import require_http_methods, require_GET

@require_GET
def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'person/person_detail.html', {'person': person})
    # return render_to_response('person/person_detail.html', {'person': person})
    # return HttpResponse(f'person: {person}')

# def person_detail(request, person_id, test):
#     try:
#         person = person.objects.get(pk=person_id)
#     except person.DoesNotExist:
#         raise Http404
#     return HttpResponse(f'person: {person} ({test})')
"""


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu_key'] = 'persons'
        return context


# @login_required
@permission_required('person.add_person')
def person_edit(request, pk):
    if pk == 'new':
        instance = None
    else:
        instance = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=instance)
    if form.is_valid():
        person = form.save()
        messages.success(request, 'Successfully saved!')
        return redirect('person_edit', pk=person.pk)
    return render(
        request,
        'person/person_edit.html',
        {
            'main_menu_key': 'persons',
            'form': form,
        },
    )
