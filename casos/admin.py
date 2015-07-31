# -*- coding: utf-8 -*-
from django.contrib import admin
from casos.models import Caso, Etapa

class CasoInline(admin.TabularInline):
    model = Etapa

class EtapaAdmin(admin.ModelAdmin):
    inlines = [CasoInline]

admin.site.register(Caso, EtapaAdmin)