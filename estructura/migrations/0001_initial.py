# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('activo', models.BooleanField(default='true')),
            ],
        ),
        migrations.CreateModel(
            name='gerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('activo', models.BooleanField(default='true')),
            ],
        ),
        migrations.CreateModel(
            name='region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(blank=True, max_length=200)),
                ('activo', models.BooleanField(default='true')),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='gerencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.gerencia'),
        ),
    ]
