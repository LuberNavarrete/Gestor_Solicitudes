# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requerimiento', '0002_auto_20180325_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='completado',
            field=models.BooleanField(editable=False),
        ),
    ]
