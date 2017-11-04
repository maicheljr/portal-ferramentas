# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0004_ferramenta_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Usuario'),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='nivel_aluno',
            field=models.CharField(choices=[('iniciante', 'Iniciante'), ('intermediário', 'Intermediário'), ('profissional', 'Profissional')], default='iniciante', max_length=15, verbose_name='nivel de experiência do Aluno'),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='nivel_professor',
            field=models.CharField(choices=[('iniciante', 'Iniciante'), ('intermediário', 'Intermediário'), ('profissional', 'Profissional')], default='iniciante', max_length=15, verbose_name='nivel de experiência do Professor'),
        ),
    ]
