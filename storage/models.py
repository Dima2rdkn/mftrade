from django.db import models

from documents.invoice.models import Invoice
from references.article.models import Article
from references.stock.models import Stock


# Регистр движений складов
class Storage(models.Model):
    STATUS_CHOICES = (
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
        ('off', 'Списание'),
    )
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT,
                              verbose_name='Склад')
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT,
                                verbose_name='Накладная')
    oper_date = models.DateTimeField(db_index=True,
                                     verbose_name='Дата операции')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              db_index=True, verbose_name='Вид операции')
    product = models.ForeignKey(Article, on_delete=models.PROTECT,
                                verbose_name='Номенклатура')
    quantity = models.DecimalField(max_digits=19, decimal_places=3,
                                   verbose_name='Количество')
    price = models.DecimalField(max_digits=19, decimal_places=2,
                                verbose_name='Цена')
    discont = models.DecimalField(max_digits=19, decimal_places=2,
                                  verbose_name='Скидка')
    summa = models.DecimalField(max_digits=19, decimal_places=2,
                                verbose_name='Сумма')
