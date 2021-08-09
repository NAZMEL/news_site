from django.contrib import admin
from django.forms import widgets
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

    # it shows values we want to see in django.admin
    list_display = (
        'id',
        'title',
        'category',
        'content',
        'views',
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

    # edit it using check-boxes
    list_editable = ('is_published', )

    # create frame for filtering 
    list_filter = (
        'is_published',
        'category'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )

    list_display_links = (
        'id',
        'title'
    )

    search_fields = ('title',  )


