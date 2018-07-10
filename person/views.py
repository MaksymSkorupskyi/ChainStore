from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from person.models import Person


def person_list(request):
    return render(request, 'person/person_list.html', {
        'persons': Person.objects.all()
        ,
        'main_menu_key': 'persons',
    })


class PersonList(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'person/person_list.html'

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'persons'
        return context


def person_detail(request, pk):
    return render(request, 'person_detail.html', {
        'person': get_object_or_404(Person, pk=pk),
        'main_menu_key': 'persons',
    })


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
