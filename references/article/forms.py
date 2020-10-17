from django import forms

from .models import ArticleGroup, Article


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = ArticleGroup
        fields = ['title', 'parent', 'description']


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        #        fields = ['title', 'article', 'category', 'image', 'description',
        #                 'supplier', 'unit_m', 'size_w', 'size_h', 'size_d', 'weight']
        # Можно использовать
        fields = '__all__'
