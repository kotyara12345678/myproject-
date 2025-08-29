from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from rest_framework import generics, permissions
from .serializers import ArticleSerializer  # DRF сериализатор
from .forms import ArticleForm  # форма для HTML

# ==========================
# Страницы сайта
# ==========================

def index_page(request):
    articles = Article.objects.order_by('-data')  
    return render(request, 'index/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'index/article_detail.html', {'article': article})

# ==========================
# DRF API для создания статьи
# ==========================

class ArticlesCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]  # доступ только с JWT

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ==========================
# HTML-форма для создания статьи
# ==========================

def create_article_page(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('index:index')  # или на детальную страницу статьи
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})