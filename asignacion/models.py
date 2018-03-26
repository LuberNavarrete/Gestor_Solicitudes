# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from personal.models import personal
from requerimiento.models import tarea

PRIORIDAD = ((1, 'Baja'),(2, 'Normal'),	(3, 'Alta'),)

# Crear signal pra que cuando se asigne una tarea se modifique el estatus de la tarea a asignado
class asignar(models.Model):
	analista = models.ForeignKey(personal,limit_choices_to={'activo': True,'analista': True})
	tarea = models.ForeignKey(tarea,limit_choices_to={'estado': 'Nueva', 'activo': True})
	prioridad = models.IntegerField(choices = PRIORIDAD, default = 2)
	creado = models.DateTimeField(auto_now_add = True, editable=False, null = True, blank = True)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=100, blank = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
        	return str(self.id)
