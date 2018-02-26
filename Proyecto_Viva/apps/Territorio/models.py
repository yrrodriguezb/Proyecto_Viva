# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Pais(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2, verbose_name="Código")
    descripcion = models.CharField(max_length=254, verbose_name="Descripción")

    class Meta:
        db_table = "Paises"
        ordering = ["descripcion"]
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class Ciudad(models.Model):
    
    CHOICES_PAISES = [ (q.codigo, q.descripcion) for q in Pais.objects.all() ]

    codigo_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="Codigo Pais", choices=CHOICES_PAISES)
    descripcion = models.CharField(max_length=254, verbose_name="Descripción")

    class Meta:
        db_table = "Ciudades"
        ordering = ["codigo_pais", "descripcion"]
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.descripcion
    
    def __unicode__(self):
        return self.descripcion


class Localidad(models.Model):
    codigo = models.CharField(primary_key=True, max_length=2, verbose_name="Codigo")
    codigo_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    descripcion = models.CharField(max_length=254, verbose_name="Descripción")

    class Meta:
        db_table = "Localidades"
        ordering = ["codigo_ciudad", "descripcion"]
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion
