from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404

from references.article.models import ArticleGroup, Article
from .forms import GroupCreateForm, ArticleCreateForm


def article_list(request, group_id=None):
    group = None
    groups = ArticleGroup.objects.all()
    articles = Article.objects.all()
    if group_id:
        group = get_object_or_404(ArticleGroup, pk=group_id)
        groups = groups.filter(parent=group)
        articles = articles.filter(category=group)
    return render(request, 'references/article/list.html',
                  {'group': group, 'groups': groups, 'articles': articles})


def article_group_edit(request, group_id=None):
    if group_id is not None:
        group = get_object_or_404(ArticleGroup, pk=group_id)
    else:
        group = ArticleGroup()
    error = 0
    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)
        if "Edit" in request.POST:
            if form.is_valid():
                cd = form.cleaned_data
                group.title = cd['title']
                group.parent = cd['parent']
                group.description = cd['description']
                group.save()
        elif "Delete" in request.POST:
            try:
                group.delete()  # удаление категории
            except ProtectedError:
                # тут нужно нормально переписать обработку ошибок
                error = 1
                return render(request, 'references/article/group.html',
                              {'group': group, 'form': form, 'error': error})
            return render(request, 'references/article/list.html')
        return render(request, 'references/article/list.html',
                      {'group': group})
    else:
        form = GroupCreateForm(instance=group)
    return render(request, 'references/article/group.html',
                  {'group': group, 'form': form, 'error': error})


def article_detail(request, article_id=None):
    if article_id is not None:
        article = get_object_or_404(Article, pk=article_id)
    else:
        article = Article()
    error = 0
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST, request.FILES, instance=article)
        if "Edit" in request.POST:
            if form.is_valid():
                form.save()
        elif "Delete" in request.POST:
            try:
                article.delete()  # удаление категории
            except ProtectedError:
                # тут нужно нормально переписать обработку ошибок
                error = 1
                return render(request, 'references/article/detail.html',
                              {'article': article,
                               'form': form,
                               'error': error})
        return render(request, 'references/article/list.html',
                      {'group': article.category})
    else:
        form = ArticleCreateForm(instance=article)
    return render(request, 'references/article/detail.html',
                  {'article': article, 'form': form, 'error': error})
