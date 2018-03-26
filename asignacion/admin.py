# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import asignar

class asignaradmin(admin.ModelAdmin):
        search_fields = ['tarea']
        list_display = ('analista','tarea','prioridad','observacion','activo')
        list_filter = ['activo','tarea']

admin.site.register(asignar,asignaradmin)
