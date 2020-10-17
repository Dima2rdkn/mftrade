from django.db import models
from django.urls import reverse

from ..contragent.models import Contragent
from ..measure.models import Measure


# Create your models here.


# Справочник группа товаров
class ArticleGroup(models.Model):
    title = models.CharField(max_length=32, unique=True, db_index=True,
                             verbose_name='Наименование')
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.SET_NULL,
                               verbose_name='Группа')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Группа товара'
        verbose_name_plural = 'Группы товара'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('references:article_list_by_group', args=[self.id])


# Справочник товаров
class Article(models.Model):
    title = models.CharField(max_length=128, unique=True, db_index=True,
                             verbose_name='Наименование')
    article = models.CharField(max_length=32, db_index=True,
                               verbose_name='Артикул')
    category = models.ForeignKey(ArticleGroup, on_delete=models.PROTECT,
                                 db_index=True, verbose_name='Группа')
    image = models.ImageField(blank=True, upload_to='images/goods/',
                              verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    supplier = models.ForeignKey(Contragent, on_delete=models.PROTECT,
                                 blank=True, null=True,
                                 verbose_name='Производитель')
    unit_m = models.ForeignKey(Measure, on_delete=models.PROTECT,
                               null=True, verbose_name='Ед.изм.')
    size_w = models.PositiveIntegerField(blank=True, null=True,
                                         verbose_name='Длина')
    size_h = models.PositiveIntegerField(blank=True, null=True,
                                         verbose_name='Высота')
    size_d = models.PositiveIntegerField(blank=True, null=True,
                                         verbose_name='Ширина')
    weight = models.PositiveIntegerField(blank=True, null=True,
                                         verbose_name='Масса')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('references:article_detail', args=[self.id])
