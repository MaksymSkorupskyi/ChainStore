from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response


def main(request):
    # person = get_object_or_404(Person, pk=person_id)
    return render(request, 'main.html')


# def start_page(request):
#     return HttpResponse(f'<h1>Chain Store</h1>')


# def main(request, i=0, j=0):
#     return HttpResponse(f'<h1>Chain Store</h1><p>{i} {j}</p>')


def post(request, slug):
    return HttpResponse(f'Post {slug}')


def http404(request):
    return HttpResponse('404')
