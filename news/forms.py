from typing import Text
from django import forms
from django.db import models
from django.forms import widgets
from .models import Category
from .models import News          # for adding form with the created db
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(label='Email', widget=widgets.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', help_text='Password must include 8 or more symbols!', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2'
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ContactForm(forms.Form):
    subject = forms.CharField(label='Article', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5 }))
