from typing import Text
from django import forms
from .models import Category
from .models import News          # for adding form with the created db
import re
from django.core.exceptions import ValidationError


# class NewsForm(forms.Form):
#     '''
#     Form for adding a new news
#     '''
#     title = forms.CharField(label='Title', max_length=150, widget=forms.TextInput(attrs={
#         "class": "form-control",                            # widget for properties into tegs
#     }))    

#     content = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
#         "class": "form-control",
#         "rows": 5,
#     }))

#     is_published = forms.BooleanField(label='Is published?: ', initial=True)                # generate check-box, initial is true for default
    
#     category = forms.ModelChoiceField(empty_label='Select category', label='Category', queryset=Category.objects.all(), widget=forms.Select(attrs={
#         "class": "form-control",
#     }))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'          # show all model fields
        fields = [
            'title',
            'content',
            'is_published',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    # validator for field title
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title can\'t start with number')
        return title
