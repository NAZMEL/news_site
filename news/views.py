from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category



def index(request):
    '''
    Get all news starting with the latest one
    '''
    news = News.objects.order_by("-created_at")
    categories = Category.objects.all()

    context = {
        'news': news, 
        'title': 'News list',
        'categories': categories
        }

    return render(request, 'news/index.html', context = context)


def get_category(request, category_id):
    '''
    Gat news for for specific category
    '''
    news = News.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)

    context = {
        'news': news,
        'categories': categories,
        'category': category
    }

    return render(request,'news/category.html', context)

