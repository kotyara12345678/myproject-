from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'image']  # добавляем поле image не обязательно вроде ну я добавил