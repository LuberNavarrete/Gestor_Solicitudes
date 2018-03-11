# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import tipo, personal

class tipoadmin(admin.ModelAdmin):
        search_fields = ['nombre']
        list_display = ('nombre','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(tipo,tipoadmin)

class personaladmin(admin.ModelAdmin):
        search_fields = ['email','nombres']
        list_display = ('email','nombres','tipo_trabajador','cargo','region','extension','observacion')
        list_filter = ['email','nombres']

admin.site.register(personal,personaladmin)
