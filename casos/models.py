from django.db import models

class Caso(models.Model):
    nombre=models.CharField('Caso', max_length=500, blank=False)
    descripcion=models.TextField('Descripcion', blank=True)

    class Meta:
        verbose_name='Caso'
        verbose_name_plural='Casos'

    def __unicode__(self):
        return '%s' % self.nombre

class Etapa(models.Model):
    nombre=models.CharField('Etapa', max_length=500, blank=False)
    descripcion=models.TextField('Descripcion', blank=True)
    caso=models.ForeignKey(Caso, verbose_name='Caso', related_name='etapa')

    class Meta:
        verbose_name='Etapa'
        verbose_name_plural='Etapas'

    def __unicode__(self):
        return '%s' % self.nombre