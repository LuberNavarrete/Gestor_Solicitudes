# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class gerencia(models.Model):
	nombre = models.CharField(max_length=100, unique = True)
	creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=100, blank = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre

class region(models.Model):
	nombre = models.CharField(max_length=100)
	creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=100, blank = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre

class cargo(models.Model):
	gerencia = models.ForeignKey(gerencia,limit_choices_to={'activo': True})
	nombre = models.CharField(max_length=100, unique = True)
	creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=100, blank = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre
