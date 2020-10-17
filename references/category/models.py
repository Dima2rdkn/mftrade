from django.db import models


# Create your models here.


# Справочник Группы
class Category(models.Model):
    title = models.CharField(max_length=32, unique=True, db_index=True,
                             verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
