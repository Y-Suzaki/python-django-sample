from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'login_name': 'guest'
    }
    return render(request, 'myapp/index.html', context)


def hello(request):
    return HttpResponse('Hello Django.')

