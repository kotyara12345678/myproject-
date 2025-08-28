from django.urls import path
from . import views

app_name = 'index'

path('index/', views.index_page, name='index'), 