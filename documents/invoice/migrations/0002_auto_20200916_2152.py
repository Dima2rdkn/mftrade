# Generated by Django 3.1.1 on 2020-09-16 21:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contragent', '0001_initial'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('invoice_date', 'status', 'supplier'),
                     'verbose_name': 'Накладная',
                     'verbose_name_plural': 'Накладные'},
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(
                choices=[('buy', 'Покупка'), ('sell', 'Продажа'),
                         ('off', 'Списание')], db_index=True,
                default=django.utils.timezone.now, max_length=10,
                verbose_name='Вид операции'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoicetable',
            name='discont',
            field=models.DecimalField(decimal_places=2, default=0.0,
                                      max_digits=19, verbose_name='Скидка'),
        ),
        migrations.AddField(
            model_name='invoicetable',
            name='summa',
            field=models.DecimalField(decimal_places=2, default=0.0,
                                      max_digits=19, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='supplier',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='contragent.contragent',
                                    verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='invoicetable',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0,
                                      max_digits=19, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='invoicetable',
            name='quantity',
            field=models.DecimalField(decimal_places=3, default=0,
                                      max_digits=19,
                                      verbose_name='Количество'),
        ),
    ]
