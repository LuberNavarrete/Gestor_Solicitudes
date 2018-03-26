# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from estructura.models import cargo, region

TipoContract = ((1, 'Contrato Tiempo Determinado'),(2, 'Contrato Tiempo Indeterminado'),)

class personal(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo_trabajador = models.IntegerField(choices = TipoContract, default = 1)
    fecha_fin = models.DateField(null = True, blank = True)
    analista = models.BooleanField()
    cargo = models.ForeignKey(cargo,limit_choices_to={'activo': True}, null = True, blank = True)
    region = models.ForeignKey(region,limit_choices_to={'activo': True}, null = True, blank = True)
    extension = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add = True, editable=False)
    modificado = models.DateTimeField(auto_now = True, editable=False)
    observacion = models.TextField(max_length=100, blank = True)
    activo = models.BooleanField(default = 'true')

    def __str__(self):
        return self.nombres
