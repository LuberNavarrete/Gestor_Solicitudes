# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requerimiento', '0003_auto_20180325_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='completado',
            field=models.CharField(default='Nueva', editable=False, max_length=100),
        ),
    ]
