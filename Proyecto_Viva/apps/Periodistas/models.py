# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..Territorio.models import Ciudad, Localidad


class Zona(models.Model):
    descripcion = models.CharField(max_length=254, verbose_name="Descripción")

    class Meta:
       verbose_name = "Zona"
       verbose_name_plural = "Zonas"

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class MedioComunicacion(models.Model):
    nombre_medio = models.CharField(max_length=254, verbose_name="Nombre del Medio")
    localidad = models.ForeignKey(Localidad, verbose_name="Localidad")
    representante_legal = models.CharField(max_length=254, verbose_name="Representante legal")
    correo_electronico = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=100, blank=True, null=True, verbose_name="Teléfono")
    direccion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dirección")
    estado = models.CharField(max_length=254, blank=True, null=True, verbose_name="Estado")
    nombre = models.CharField(max_length=254, blank=True, null=True, verbose_name="Nombre")
    cedula = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cédula")
    ciudad = models.ForeignKey(Ciudad, blank=True, null=True, verbose_name="Ciudad")
    zona = models.ForeignKey(Zona, verbose_name="Zona")

    class Meta:
        verbose_name = "Medio de Comunicación"
        verbose_name_plural = "Medios de Comunicación"

    def __str__(self):
        return self.nombre_medio

    def __unicode__(self):
        return self.nombre_medio