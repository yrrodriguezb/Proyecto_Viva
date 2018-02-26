# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MedioComunicacion, Zona


class MedioComunicacionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_medio", "localidad", "representante_legal",)
    ordering = ["nombre_medio", "localidad",]
    search_fields = ["nombre_medio", "representante_legal",]

class ZonaAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion",)
    ordering = ["descripcion",]


admin.site.register(MedioComunicacion, MedioComunicacionAdmin)
admin.site.register(Zona, ZonaAdmin)

