from django.shortcuts import render
from django.http import HttpResponse

# Добавьте эту функцию если её нет
def index_page(request):
    return HttpResponse("Главная страница")
    # или
    return render(request, "index.html")