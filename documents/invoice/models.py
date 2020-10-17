from django.conf import settings
from django.db import models
from django.urls import reverse

from references.article.models import Article
from references.contragent.models import Contragent
from references.measure.models import Measure
from references.stock.models import Stock


# Create your models here.


# документ Накладная
class Invoice(models.Model):
    STATUS_CHOICES = (
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
        ('off', 'Списание'),
        ('return', 'Возврат'),
        ('inventory', 'Инвентаризация'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.PROTECT,
                                verbose_name='Автор')
    number = models.CharField(max_length=32, verbose_name='Номер')
    invoice_date = models.DateTimeField(verbose_name='Дата')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              db_index=True, verbose_name='Вид операции')
    supplier = models.ForeignKey(Contragent, null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Поставщик')
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT,
                              verbose_name='Склад')
    summa = models.DecimalField(max_digits=19, decimal_places=2,
                                verbose_name='Сумма')

    class Meta:
        ordering = ('invoice_date', 'status', 'supplier',)
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'

    def __str__(self):
        return 'Накладная № {} от {}'.format(self.number, self.invoice_date)

    def get_absolute_url(self):
        return reverse('documents:stock_detail',
                       kwargs={'pk': self.pk})


class InvoiceTable(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,
                                verbose_name='Документ')
    product = models.ForeignKey(Article, on_delete=models.PROTECT,
                                verbose_name='Номенклатура')
    quantity = models.DecimalField(max_digits=19, decimal_places=3, default=0,
                                   verbose_name='Количество')
    mesure = models.ForeignKey(Measure, on_delete=models.PROTECT,
                               verbose_name='Ед.изм.')
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0.00,
                                verbose_name='Цена')
    discont = models.DecimalField(max_digits=19, decimal_places=2,
                                  default=0.00, verbose_name='Скидка')
    summa = models.DecimalField(max_digits=19, decimal_places=2,
                                default=0.00, verbose_name='Сумма')
