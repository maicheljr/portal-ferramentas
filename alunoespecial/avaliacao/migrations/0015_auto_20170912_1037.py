# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0014_auto_20170912_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferramenta',
            name='nivel_aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avaliacao.NivelDicente'),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='nivel_professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avaliacao.NivelDocente'),
        ),
    ]
