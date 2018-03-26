# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import categoria, tarea

class categoriaadmin(admin.ModelAdmin):
        search_fields = ['nombre']
        list_display = ('nombre','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(categoria,categoriaadmin)

class tareaadmin(admin.ModelAdmin):
        search_fields = ['categoria']
        list_display = ('categoria','descripcion','estado','usuario','activo')
        list_filter = ['activo','categoria']

admin.site.register(tarea,tareaadmin)
