from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    """ IndexView
    対応するtemplate: day_list.html
    """
    model = Day
    paginate_by = 3

    # template名を指定することも可能
    # template_name = 'diary/day_list.html'


class AddView(generic.CreateView):
    """ AddView
    対応するtemplate: day_form.html
    templateに渡される変数: form, day
    """
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')  # リダイレクト先


class UpdateView(generic.UpdateView):
    """ UpdateView
    対応するtemplate: day_form.html
    templateに渡される変数: form, day
    """
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')  # リダイレクト先


class DeleteView(generic.DeleteView):
    """ DeleteView
    対応するtemplate: day_confirm_delete.html
    templateに渡される変数: day
    """
    model = Day
    success_url = reverse_lazy('diary:index')  # リダイレクト先


class DetailView(generic.DetailView):
    """ DetailView
    対応するtemplate: day_detail.html
    templateに渡される変数: day
    """
    model = Day

