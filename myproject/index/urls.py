from django.urls import path
from . import views
from .views import ArticlesCreateView

app_name = 'index'

urlpatterns = [
    path('', views.index_page, name='index'),  # главная страница со списком статей
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # просмотр статьи
    path('create/', ArticlesCreateView.as_view(), name='create_article'),  # создание через DRF API
    path('create-page/', views.create_article_page, name='create_article_page'),  # создание через HTML-форму
]