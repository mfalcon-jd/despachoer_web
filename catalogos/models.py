from django.db import models

class Telefono(models.Model):
    TIPO_CHOICES =(
        ('CASA', 'Casa'),
        ('CELULAR', 'Celular'),
    )
    telefono = models.CharField(max_length=10, blank=True, null=true)
    cliente = models.ForeignKey(Cliente, related_name='cliente_id')
    agenda = models.ForeignKey(Agenda, related_name='agenda_id')