# Generated by Django 3.1.1 on 2020-09-15 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title',
                 models.CharField(db_index=True, max_length=128, unique=True,
                                  verbose_name='Наименование')),
                ('article', models.CharField(db_index=True, max_length=32,
                                             verbose_name='Артикул')),
                ('image',
                 models.ImageField(blank=True, upload_to='images/goods/')),
                ('description',
                 models.TextField(blank=True, verbose_name='Описание')),
                ('size_w', models.PositiveIntegerField(blank=True)),
                ('size_h', models.PositiveIntegerField(blank=True)),
                ('size_d', models.PositiveIntegerField(blank=True)),
                ('weight', models.PositiveIntegerField(blank=True)),
                ('category',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   to='category.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
