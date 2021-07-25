from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Name of article')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Publish date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update date')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Is published?')                      # is_published = 1

    def __str__(self):
        return self.title

    # class for django.admin
    class Meta:
        verbose_name = 'Новина'         # singular name of table
        verbose_name_plural = 'Новини'   # plural name
        ordering = ['-created_at']