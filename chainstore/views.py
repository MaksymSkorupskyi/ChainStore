from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from chainstore.forms import SendMessageForm, DivErrorList
from django.contrib.auth.views import LoginView


# @login_required
def main(request):
    return render(request, 'main.html')
    # return render(request, 'main.html', {'a': 1})


# Forms experiments _____________________________________________
def message_form(request):
    # if request.method == 'POST':
    #     print(request.POST)
    #     messages.success(request, 'OK')
    #     return redirect('message-form')
    form = SendMessageForm(
        request.POST or None,
        initial={'name': 'your name'},
        # auto_id=True,
        # label_suffix=' ->',
        # prefix='test',
        error_class=DivErrorList,
    )
    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['message'])
        messages.success(request, 'OK')
        return redirect('message-form')
    return render(request, 'chainstore/message_form.html', {'form': form})


# request methods demonstration
def start_page(request):
    print(request.scheme)
    print(request.path)
    print(request.get_host())
    print(request.get_full_path())
    print(request.build_absolute_uri())
    print(request.build_absolute_uri('main/'))
    print(request.is_secure())
    print(request.is_ajax())
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.user)
    print(request.session)
    print(request.REQUEST)
    if 'i' not in request.session:
        request.session['i'] = 1
    else:
        request.session['i'] += 1
    print(request.session['i'])
    for i in request.META.items():
        print('{} = {}'.format(*i))

    return HttpResponse('<h1>Chain Store<form method="post"><input type="text" name="a"><input type="submit"></form>')
    # return HttpResponse('<h1>Chain Store</h1>')


# def main(request, i=0, j=0):
#     return HttpResponse(f'<h1>Chain Store</h1><p>{i} {j}</p>')


def post(request, slug):
    return HttpResponse(f'Post {slug}')


def http404(request):
    return HttpResponse('404')
