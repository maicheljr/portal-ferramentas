# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0012_niveldicente_niveldocente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ferramenta',
            name='nivel_aluno',
        ),
        migrations.RemoveField(
            model_name='ferramenta',
            name='nivel_professor',
        ),
    ]
