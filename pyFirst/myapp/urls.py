from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info')
]
