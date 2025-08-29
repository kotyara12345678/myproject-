from django.urls import path

from accounts.urls import urlpatterns
from . import views

app_name = 'index'

urlpatterns = [
    path('index/', views.index_page, name='index'),
]
