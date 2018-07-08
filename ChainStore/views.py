from django.http import HttpResponse

def start_page(request):
    return HttpResponse(f'<h1>Chain Store</h1>')

def main(request, i=0, j=0):
    return HttpResponse(f'<h1>Chain Store</h1><p>{i} {j}</p>')


def post(request, slug):
    return HttpResponse(f'Post {slug}')


def http404(request):
    return HttpResponse('404')
