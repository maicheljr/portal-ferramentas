# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0013_auto_20170912_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferramenta',
            name='nivel_aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete='id', to='avaliacao.NivelDicente', to_field='nome'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='nivel_professor',
            field=models.ForeignKey(blank=True, null=True, on_delete='id', to='avaliacao.NivelDocente', to_field='nome'),
        ),
    ]
