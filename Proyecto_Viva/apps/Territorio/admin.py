# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import  Ciudad, Localidad, Pais


class CiudadAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo_pais", "descripcion",)
    ordering = ["codigo_pais", "descripcion",]
    search_fields = ["codigo_pais__descripcion", "descripcion",]


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ("codigo", "codigo_ciudad", "descripcion",)
    ordering = ["codigo",]


class PaisAdmin(admin.ModelAdmin):
    list_display  = ("codigo", "descripcion",)
    search_fields = ["codigo", "descripcion",]


admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Pais, PaisAdmin)