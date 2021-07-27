from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category



def index(request):
    '''
    Get all news starting with the latest one
    '''
    news = News.objects.order_by("-created_at")

    context = {
        'news': news, 
        'title': 'News list',
        }

    return render(request, 'news/index.html', context = context)


def get_category(request, category_id):
    '''
    Gat news for specific category
    '''
    news = News.objects.filter(category_id = category_id)
    category = Category.objects.get(pk = category_id)

    context = {
        'news': news,
        'category': category
    }

    return render(request,'news/category.html', context)


def view_news(request, news_id):
    '''
    Get all information about news
    '''
    news_item = get_object_or_404(News, pk = news_id)
    
    context = {
        'news_item': news_item
    }

    return render(request, 'news/view_news.html', context)