# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-13 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abaco', '0022_auto_20200113_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoracionidea',
            name='justificacion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='valoracionidea',
            name='valoracion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abaco.OpcionEscala'),
        ),
    ]
