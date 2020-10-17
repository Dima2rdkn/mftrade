# Generated by Django 3.1.1 on 2020-09-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('article', '0002_auto_20200915_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title',
                 models.CharField(db_index=True, max_length=32, unique=True,
                                  verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Группа товара',
                'verbose_name_plural': 'Группы товара',
            },
        ),
    ]
