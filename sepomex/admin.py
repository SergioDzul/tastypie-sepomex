# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MXEstado, MXMunicipio, MXCiudad, MXAsentamiento

# Register your models here.
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abbr')
    search_fields = ('nombre',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clave', 'mx_estado')
    list_filter = ('mx_estado',)
    search_fields = ('nombre', 'clave')

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mx_estado')
    list_filter = ('mx_estado',)
    search_fields = ('nombre',)

class AsentamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mx_ciudad', 'mx_municipio', 'tipo_asentamiento', 'zona', 'cp')
    list_filter = ('zona',)
    search_fields = ('cp', 'nombre')

admin.site.register(MXEstado, EstadoAdmin)
admin.site.register(MXMunicipio, MunicipioAdmin)
admin.site.register(MXCiudad, CiudadAdmin)
admin.site.register(MXAsentamiento, AsentamientoAdmin)
