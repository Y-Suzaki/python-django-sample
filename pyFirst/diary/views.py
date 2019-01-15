from django.shortcuts import render, redirect
from .forms import DayCreateForm


def index(request):
    """ index """
    context = {
        'login_name': 'guest'
    }
    return render(request, 'diary/day_list.html', context)


def add(request):
    """ add
    初回時はGET、Form送信時はPOSTで本メソッドが呼ばれる。
    """
    form = DayCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'login_name': 'guest',
        'form': DayCreateForm()
    }
    return render(request, 'diary/day_form.html', context)

