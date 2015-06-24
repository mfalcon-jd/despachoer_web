from django.db import models

class Cliente(models.Model):
    curp = models.CharField(max_length=18, blank=True)
    nombre = models.CharField(max_length=250)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250, blank=True)
    fecha_nacimiento = models.DateField(blank=True)
    email = models.EmailField(max_length=250)
    observaciones = models.CharField(max_length=1000)

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __unicode__(self):
        return '%s %s, %s' %(self.apellido_paterno, self.apellido_materno, self.nombre)