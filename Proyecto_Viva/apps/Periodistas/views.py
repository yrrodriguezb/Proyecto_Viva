# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import MedioComunicacionForm
from .models import MedioComunicacion


class MedioComunicacionCreateView(CreateView):
    form_class = MedioComunicacionForm
    model = MedioComunicacion
    template_name = "Periodistas/PAgregar.html"
    success_url = reverse_lazy("MedioComunicacion:listar")

    @method_decorator(permission_required('Periodistas.add_mediocomunicacion',reverse_lazy('MedioComunicacion:listar')))
    def dispatch(self, *args, **kwargs):
        return super(MedioComunicacionCreateView, self).dispatch(*args, **kwargs)


class MedioComunicacionDeleteView(DeleteView):
    context_object_name = "medios_comunicacion"
    model = MedioComunicacion
    template_name = "Periodistas/PEliminar.html"
    success_url = reverse_lazy("MedioComunicacion:listar")

    @method_decorator(permission_required('Periodistas.delete_mediocomunicacion',reverse_lazy('MedioComunicacion:listar')))
    def dispatch(self, *args, **kwargs):
        return super(MedioComunicacionDeleteView, self).dispatch(*args, **kwargs)


class MedioComunicacionListView(ListView):
    context_object_name = "medios_comunicacion"
    model = MedioComunicacion
    paginate_by = 100
    template_name = "Periodistas/PListar.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MedioComunicacionListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            qset = (
                Q(nombre_medio__icontains=query) |
                Q(representante_legal__icontains=query) |
                Q(localidad__descripcion__icontains=query)
            )
            results = MedioComunicacion.objects.filter(qset).distinct()
        else:
            results = MedioComunicacion.objects.all()
        return results

    def get_context_data(self, **kwargs):
        context = super(MedioComunicacionListView, self).get_context_data(**kwargs)
        context['params'] = { 'query' : self.request.GET.get('q', '') }
        return context


class MedioComunicacionUpdateView(UpdateView):
    form_class = MedioComunicacionForm
    model = MedioComunicacion
    template_name = "Periodistas/PEditar.html"
    success_url = reverse_lazy("MedioComunicacion:listar")

    @method_decorator(permission_required('Periodistas.change_mediocomunicacion',reverse_lazy('MedioComunicacion:listar')))
    def dispatch(self, *args, **kwargs):
        return super(MedioComunicacionUpdateView, self).dispatch(*args, **kwargs)


def error_404(request):
    return render(request, "errores/error.html", { "primero": 4, "segundo": 0, "tercero": 4 })

def error_500(request):
    return render(request, "errores/error.html", { "primero": 5, "segundo": 0, "tercero": 0 })