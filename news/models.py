from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Name of article')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Publish date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update date')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Is published?')                      # is_published = 1
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs = {"pk": self.pk})


    # class for django.admin
    class Meta:
        verbose_name = 'Новина'         # singular name of table
        verbose_name_plural = 'Новини'   # plural name
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category name')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs = {"category_id": self.pk})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']