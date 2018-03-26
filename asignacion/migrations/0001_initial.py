# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requerimiento', '0005_auto_20180325_0916'),
        ('personal', '0003_auto_20180325_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='asignar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(blank=True, max_length=100)),
                ('activo', models.BooleanField(default='true')),
                ('analista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requerimiento.tarea')),
            ],
        ),
    ]