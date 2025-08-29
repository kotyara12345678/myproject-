from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]