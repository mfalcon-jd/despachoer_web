# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500, verbose_name=b'Caso')),
                ('descripcion', models.TextField(verbose_name=b'Descripcion', blank=True)),
            ],
            options={
                'verbose_name': 'Caso',
                'verbose_name_plural': 'Casos',
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500, verbose_name=b'Etapa')),
                ('descripcion', models.TextField(verbose_name=b'Descripcion', blank=True)),
                ('caso', models.ForeignKey(related_name='etapa', verbose_name=b'Caso', to='casos.Caso')),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
            },
        ),
    ]
