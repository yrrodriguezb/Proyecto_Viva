"""Proyecto_Viva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url, handler400, handler500
from django.conf.urls.static import static
from django.contrib import admin

from apps.Usuarios.views import index
from apps.Periodistas.views import error_404, error_500

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^mediocomunicacion/', include('apps.Periodistas.urls', namespace='MedioComunicacion')),
    url(r'^usuario/', include('apps.Usuarios.urls', namespace='Usuarios')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = error_404
handler500 = error_500