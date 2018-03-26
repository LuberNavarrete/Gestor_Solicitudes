# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from personal.models import personal

class categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=100, blank = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre

class tarea(models.Model):
    categoria = models.ForeignKey(categoria,limit_choices_to={'activo': True})
    descripcion = models.TextField(max_length=100)
    completado = models.BooleanField(editable = False)
    estado = models.CharField(default = 'Nueva', editable = False, max_length=100)
    # este debe de desaparecer por usuario que crea el requerimiento
    usuario = models.ForeignKey(personal, limit_choices_to={'activo': True})
    creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
    modificado = models.DateTimeField(auto_now = True, editable=False)
    activo = models.BooleanField(default = 'true')

    def __str__(self):
        return self.descripcion
