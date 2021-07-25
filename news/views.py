from django.shortcuts import render
from django.http import HttpResponse
from .models import News



def index(request):
    '''
    Get all news starting with the latest one
    '''
    news = News.objects.order_by("-created_at")
    context = {'news': news, 'title': 'News list'}

    return render(request, 'news/index.html', context = context)


