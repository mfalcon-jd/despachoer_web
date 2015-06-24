# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curp', models.CharField(max_length=18, blank=True)),
                ('nombre', models.CharField(max_length=250)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('apellido_materno', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=250, blank=True)),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('email', models.CharField(max_length=250)),
                ('observaciones', models.CharField(max_length=1000)),
            ],
        ),
    ]
