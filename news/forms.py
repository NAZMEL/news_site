from typing import Text
from django import forms
from .models import Category


class NewsForm(forms.Form):
    '''
    Form for adding a new news
    '''
    title = forms.CharField(label='Title', max_length=150, widget=forms.TextInput(attrs={
        "class": "form-control",                            # widget for properties into tegs
    }))    

    content = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
    }))

    is_published = forms.BooleanField(label='Is published?: ', initial=True)                # generate check-box, initial is true for default
    
    category = forms.ModelChoiceField(empty_label='Select category', label='Category', queryset=Category.objects.all(), widget=forms.Select(attrs={
        "class": "form-control",
    }))
    