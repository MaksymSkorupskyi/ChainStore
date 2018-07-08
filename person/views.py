from django.shortcuts import render, get_object_or_404, render_to_response
# from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods, require_GET
from person.models import Person


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
