# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-01 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0010_auto_20170901_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferramenta',
            name='indicacao_pedagogica',
            field=models.TextField(blank=True, max_length=100, verbose_name='Indicação de Ensino Pedagógico'),
        ),
    ]