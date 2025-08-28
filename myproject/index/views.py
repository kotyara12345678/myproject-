from django.shortcuts import render
from .models import Articles

def index_page(request):
    articles = Articles.objects.order_by('-data')  
    return render(request, 'index/index.html', {'articles': articles})