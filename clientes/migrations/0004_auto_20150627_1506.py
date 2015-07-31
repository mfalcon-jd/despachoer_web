# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20150625_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=250, verbose_name=b'Email', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observaciones',
            field=models.CharField(max_length=1000, verbose_name=b'Observaciones', blank=True),
        ),
    ]
