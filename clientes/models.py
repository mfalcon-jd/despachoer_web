# -*- coding: utf-8 -*-
from django.db import models

class Cliente(models.Model):
    curp = models.CharField('CURP o INE', max_length=18, blank=True)
    nombre = models.CharField('Nombre', max_length=250)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=200)
    apellido_materno = models.CharField('Apellido Materno', max_length=200)
    direccion = models.CharField('Direccion', max_length=250, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', blank=True)
    email = models.EmailField('Email', max_length=250, blank=True)
    observaciones = models.CharField('Observaciones', max_length=1000, blank=True)

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __unicode__(self):
        return '%s %s, %s' %(self.apellido_paterno, self.apellido_materno, self.nombre)

class Telefono(models.Model):
    TIPO_TELEFONO_CHOICES = (
        ('CASA', 'Casa'),
        ('CELULAR', 'Celular'),
    )    
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='telefono')
    telefono = models.CharField('Teléfono', max_length=10, blank=True, null=True)
    tipo_telefono = models.CharField('Tipo de Teléfono', max_length=15, blank=False, choices=TIPO_TELEFONO_CHOICES)

    class Meta:
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'
        unique_together = [('cliente', 'telefono', 'tipo_telefono'),]

    def __unicode__(self):
        return '%s' % self.telefono