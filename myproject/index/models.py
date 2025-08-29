from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

    #КЛАСС ПУБЛИКАЦИИ
class Article(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    full_text = models.TextField('Статья')
    image = models.ImageField('Фото', upload_to='articles_images/', blank=True, null=True)  #фото
    data = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
    
    
   #КЛАСС КОМЕНТАРИИ 
class coments:
        title = models.CharField('Заголовок', max_length=100)
        full_text = models.TextField('Статья') # текст статьи
        data = models.DateTimeField('Дата публикации', default=timezone.now) # дата
        
        
        def __str__(self):
             return self.title
         
          #КЛАСС ЛАЙКИ .....