from django.shortcuts import render
from django.shortcuts import render
from .models import Articles

def index_page(request):
    return render(request, 'index/index.html')


def news_home(request):
    articles = Articles.objects.order_by('-data')  # новые сначала нах
    return render(request, 'index/index.html', {'articles': articles})

