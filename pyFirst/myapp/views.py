from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """ index """
    context = {
        'login_name': 'guest'
    }
    return render(request, 'myapp/day_list.html', context)


def about(request):
    """ about """
    return render(request, 'myapp/about.html')


def info(request):
    """ info """
    return render(request, 'myapp/info.html')


def hello(request):
    return HttpResponse('Hello Django.')

