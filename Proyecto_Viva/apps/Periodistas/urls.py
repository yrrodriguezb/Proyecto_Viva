from django.conf.urls import url

from .views import (
    MedioComunicacionCreateView,
    MedioComunicacionDeleteView,
    MedioComunicacionListView,
    MedioComunicacionUpdateView
)

urlpatterns = [
    url(r'^$', MedioComunicacionListView.as_view(), name='listar'),
    url(r'^agregar/', MedioComunicacionCreateView.as_view(), name="agregar"),
    url(r'^(?P<pk>\d+)/editar/$', MedioComunicacionUpdateView.as_view(), name="editar"),
    url(r'^(?P<pk>\d+)/eliminar/', MedioComunicacionDeleteView.as_view(), name="eliminar"),
]