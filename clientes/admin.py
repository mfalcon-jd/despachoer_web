# -*- coding: utf-8 -*-
from django.contrib import admin
from clientes.models import Cliente
from clientes.models import Telefono


#admin.site.register(Telefono)

## (TAB_NAME, TAB_TITLE)

class ClienteInline(admin.TabularInline):
    model = Telefono  

class TelefonoAdmin(admin.ModelAdmin):
    inlines = [ClienteInline]

admin.site.register(Cliente, TelefonoAdmin)