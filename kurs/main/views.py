from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    context = {
        'title': 'home',
        'content': 'главная страница магазина - HOME',
        'list': [ 'first', 'second'],
        'dict': {'first': 1},
        'is_auth': False
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render(request)