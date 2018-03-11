# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from estructura.models import cargo, region

class tipo(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=200, blank = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre

class personal(models.Model):
    email = models.EmailField(unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_trabajador = models.ForeignKey(tipo,limit_choices_to={'activo': True}, null = True, blank = True)
    cargo = models.ForeignKey(cargo,limit_choices_to={'activo': True}, null = True, blank = True)
    region = models.ForeignKey(region,limit_choices_to={'activo': True}, null = True, blank = True)
    extension = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
    modificado = models.DateTimeField(auto_now = True, editable=False)
    observacion = models.TextField(max_length=200, blank = True)
    activo = models.BooleanField(default = 'true')

    def __str__(self):
        return self.email