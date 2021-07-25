from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # it shows values we want to see in django.admin
    list_display = (
        'id',
        'title',
        'content',
        'created_at',
        'updated_at',
        'is_published'
    )

    # it shows values with links we want to use in django.admin
    list_display_links = (
        'id',
        'title'
    )

    # create field for searching
    # tuple of column in which we want to look for
    search_fields = (
        'title',
        'content'
    )