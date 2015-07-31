# -*- coding: utf-8 -*-
from django.db import models

class Agenda(models.Model):
    nombre = models.CharField(max_length=150,blank=False)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    notas = models.TextField(max_length=500)