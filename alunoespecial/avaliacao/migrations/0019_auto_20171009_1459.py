# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-09 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0018_auto_20170915_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferramenta',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='avaliacao/imagem', verbose_name='Adicionar imagem'),
        ),
    ]
