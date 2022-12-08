from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data ={
        'title': 'Список аниме',
        'animes': ['Naruto','Bleach', 'Evangelion']
    }
    return render(request, 'main/index.html', data)


def about(request):
    data ={
        'title': 'Режиссёры',
        'authors': ['Масаси Кисимото', 'Тайто Кубо', 'Ёсиюки Садамото']
    }
    return render(request, 'main/about.html',data)