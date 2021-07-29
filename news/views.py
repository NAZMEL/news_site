from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm



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


def add_news(request):
    '''
    View for adding a new news
    '''
    if request.method == 'POST':
        # filling the form
        form = NewsForm(request.POST) 
        if form.is_valid():
            print(form.cleaned_data)
            news = News.objects.create(**form.cleaned_data)

            # go to the main page
            # return redirect('index')
            
            # go page with the created news
            return redirect(news)
    else:
        form = NewsForm()

    return render(request, 'news/add_news.html', context = {'form': form, })