from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # имя автора только для чтения

    class Meta:
        model = Article
        fields = ['id', 'title', 'full_text', 'image', 'data', 'author']  # убрали 'anons'
        