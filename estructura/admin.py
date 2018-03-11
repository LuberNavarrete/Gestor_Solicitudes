# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import cargo, gerencia, region

class cargoadmin(admin.ModelAdmin):
        search_fields = ['nombre','gerencia']
        list_display = ('gerencia','nombre','observacion','activo')
        list_filter = ['activo','nombre','gerencia']

admin.site.register(cargo,cargoadmin)

class gerenciaadmin(admin.ModelAdmin):
        search_fields = ['nombre']
        list_display = ('nombre','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(gerencia,gerenciaadmin)

class regionadmin(admin.ModelAdmin):
        search_fields = ['nombre']
        list_display = ('nombre','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(region,regionadmin)