from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.simple_view, name='index'),
    path('register/', views.registr_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_page, name='logout'),
]
