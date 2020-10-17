# Generated by Django 3.1.1 on 2020-09-16 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('article', '0006_auto_20200916_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlegroup',
            name='parrent',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='article.articlegroup',
                                    verbose_name='Группа'),
        ),
    ]
