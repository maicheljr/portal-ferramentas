# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0011_auto_20170901_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelDicente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='nome')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('upload_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name_plural': 'Níveis Dicente',
                'ordering': ['nome'],
                'verbose_name': 'Nível Dicente',
            },
        ),
        migrations.CreateModel(
            name='NivelDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='nome')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('upload_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name_plural': 'Níveis Docente',
                'ordering': ['nome'],
                'verbose_name': 'Nível Docente',
            },
        ),
    ]