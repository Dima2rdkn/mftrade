from django.db import models
from django.urls import reverse


# Справочник складов
class Stock(models.Model):
    title = models.CharField(max_length=32, unique=True, db_index=True,
                             verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('references:stock_detail',
                       kwargs={'pk': self.pk})
