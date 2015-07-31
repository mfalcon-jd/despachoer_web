# -*- coding: utf-8 -*-
from django.contrib import admin
from clientes.models import Cliente, Telefono

#admin.site.register(Telefono)

class ClienteInline(admin.TabularInline):
    model = Telefono  

class TelefonoAdmin(admin.ModelAdmin):
    inlines = [ClienteInline]

admin.site.register(Cliente, TelefonoAdmin)