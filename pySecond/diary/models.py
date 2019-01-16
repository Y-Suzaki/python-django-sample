from django.db import models
from django.utils import timezone


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now())

    def __str__(self):
        """ admin画面の一覧表示にも使われる """
        return self.title
