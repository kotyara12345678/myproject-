from django.shortcuts import render
from .models import Articles, get_object_or_404

def index_page(request):
    articles = Articles.objects.order_by('-data')  
    return render(request, 'index/index.html', {'articles': articles}),

def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})