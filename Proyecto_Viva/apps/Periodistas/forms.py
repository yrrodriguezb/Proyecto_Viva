# -*- coding:utf-8 -*-

from django import forms
from .models import MedioComunicacion


class MedioComunicacionForm(forms.ModelForm):

    class Meta:
        model = MedioComunicacion

        fields = [
            "nombre_medio",
            "localidad",
            "representante_legal",
            "correo_electronico",
            "telefono",
            "direccion",
            "estado",
            "nombre",
            "cedula",
            "ciudad",
            "zona"
        ]

        labels = {
            "nombre_medio": "Nombre Medio",
            "localidad": "Localidad",
            "representante_legal": "Representante Legal",
            "correo_electronico": "Correo Electrónico",
            "telefono": "Numero Teléfonico",
            "direccion": "Dirección",
            "estado": "Estado",
            "nombre": "Nombre",
            "cedula": "Número identificación",
            "ciudad": "Ciudad",
            "zona": "Zona"
        }

        widgets = {
            'nombre_medio': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
            'representante_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-control'})
        }