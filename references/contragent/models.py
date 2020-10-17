from django.db import models
from django.urls import reverse


# Контрагент


class Contragent(models.Model):
    title = models.CharField(max_length=64, db_index=True,
                             verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('references:contragent_detail',
                       kwargs={'pk': self.pk})
