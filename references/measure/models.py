from django.db import models
from django.urls import reverse


# Справочник Единицы измерения


class Measure(models.Model):
    title = models.CharField(max_length=8, unique=True, db_index=True,
                             verbose_name='Наименование')
    description = models.CharField(max_length=64, verbose_name='Описание')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('references:measure_detail',
                       kwargs={'pk': self.pk})
