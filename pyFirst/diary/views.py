from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day


def index(request):
    """ index """
    context = {
        'login_name': 'guest',
        'day_list': Day.objects.all()
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


def update(request, pk):
    """ update
    pkが引数で渡ってくるため、DBからデータを取得する。
    初回時はそのデータをフォームに表示させる。それ以外は新規登録時と変わらない。
    """
    day = get_object_or_404(Day, pk=pk)
    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'login_name': 'guest',
        'form': form
    }
    return render(request, 'diary/day_form.html', context)


def delete(request, pk):
    """ delete
    pkが引数で渡ってくるため、DBからデータを取得する。
    Formではないため、validationは不要。
    最初に削除確認画面を表示→POSTにて削除リクエストとなる。
    """
    day = get_object_or_404(Day, pk=pk)

    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    context = {
        'day': day
    }
    return render(request, 'diary/day_confirm_delete.html', context)

