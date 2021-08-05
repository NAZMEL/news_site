from django import template
from news.models import Category
from django.db.models import Count


register = template.Library()


@register.simple_tag(name = 'get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # show categories where 1 ore more objects are
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)

    context = {
        'categories': categories
    }

    return context
