# -*- coding: utf-8 -*-
from django.db import models
from clientes.models import Cliente
from casos.models import Caso, Etapa

class Tramite(models.Model):
    TIPO_PAGO_CHOICES = (
        ('CONTADO', 'Contado'),
        ('ABONO', 'Abono'),
    )

    ESTATUS_CHOICES = (
        ('EN_PROCESO', 'En Proceso'),
        ('TERMINADO', 'Terminado'),
        ('CANCELADO', 'Cancelado'),
    )

    observaciones = models.TextField('Observaciones', blank=True)
    tipo_pago = models.CharField('Tipo de Pago', max_length=10, blank=True, choices=TIPO_PAGO_CHOICES)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = modesl.DateField(auto_now_add=True)
    fecha_finalizacion = models.DateField(auto_now_add=True)
    anticipo = models.DecimalField('Anticipo', blank=True)
    estatus = models.CharField('Estatus', max_length=15, blank=False, choices=ESTATUS_CHOICES)
    pagado = models.BooleanField('Pagado', default=False)
    precio = models.DecimalField('Precio', blank=False)
    numero_tramite = models.CharField('Numero de Tramite', max_length=25, blamk=True)
    cliente = models.ForeingKey(Cliente, verbose_name='Cliente')

    class Meta:
        verbose_name = 'Tramite'
        verbose_name_plural = 'Tramites'

    def __unicode__(self):
        return '%s' %(self.numero_tramite)