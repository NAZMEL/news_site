from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeNews(ListView):
    # template = news_list
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published = True).select_related('category')

# def index(request):
#     '''
#     Get all news starting with the latest one
#     '''
#     news = News.objects.order_by("-created_at")

#     context = {
#         'news': news, 
#         'title': 'News list',
#         }

#     return render(request, 'news/index.html', context = context)

class NewsByCategory(ListView):
    # template = news_list
    model = News
    context_object_name = 'news'
    allow_empty = False             # don't show empty list

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published = True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk = self.kwargs['category_id'])
        return context
    


# def get_category(request, category_id):
#     '''
#     Gat news for specific category
#     '''
#     news = News.objects.filter(category_id = category_id)
#     category = Category.objects.get(pk = category_id)

#     context = {
#         'news': news,
#         'category': category
#     }

#     return render(request,'news/category.html', context)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


# def view_news(request, news_id):
#     '''
#     Get all information about news
#     '''
#     news_item = get_object_or_404(News, pk = news_id)
    
#     context = {
#         'news_item': news_item
#     }

#     return render(request, 'news/view_news.html', context)


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url = reverse_lazy('index')


# for case where form connected with model
# def add_news(request):
#     '''
#     View for adding a new news
#     '''
#     if request.method == 'POST':
#         # filling the form
#         form = NewsForm(request.POST) 
#         if form.is_valid():
#             ################
#             news = form.save()

#             return redirect(news)
#     else:
#         form = NewsForm()

#     return render(request, 'news/add_news.html', context = {'form': form, })


# for case where form isn't connected with model
# def add_news(request):
#     '''
#     View for adding a new news
#     '''
#     if request.method == 'POST':
#         # filling the form
#         form = NewsForm(request.POST) 
#         if form.is_valid():
#             print(form.cleaned_data)
#             news = News.objects.create(**form.cleaned_data)

#             # go to the main page
#             # return redirect('index')
            
#             # go page with the created news
#             return redirect(news)
#     else:
#         form = NewsForm()

#     return render(request, 'news/add_news.html', context = {'form': form, })


