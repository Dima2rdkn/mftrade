# Generated by Django 3.1.1 on 2020-09-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
