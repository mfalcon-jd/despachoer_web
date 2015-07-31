# -*- coding: utf-8 -*-
from django.db import models

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

    observaciones = models.TextField('Observaciones', blakc=True)
    tipo_pago