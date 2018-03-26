# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import personal

class personaladmin(admin.ModelAdmin):
        search_fields = ['email','nombres']
        list_display = ('nombres','apellidos','email','tipo_trabajador','cargo','region','extension','observacion')
        list_filter = ['email','nombres','analista']

admin.site.register(personal,personaladmin)
