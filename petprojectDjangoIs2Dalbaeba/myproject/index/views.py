from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Index page works!")


def index_page():
    return None