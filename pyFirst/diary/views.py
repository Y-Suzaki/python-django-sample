from django.shortcuts import render


def index(request):
    """ index """
    context = {
        'login_name': 'guest'
    }
    return render(request, 'diary/day_list.html', context)
