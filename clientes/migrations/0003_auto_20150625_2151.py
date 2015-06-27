# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20150624_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.CharField(max_length=10, null=True, verbose_name=b'Tel\xc3\xa9fono', blank=True)),
                ('tipo_telefono', models.CharField(max_length=15, verbose_name=b'Tipo de Tel\xc3\xa9fono', choices=[(b'CASA', b'Casa'), (b'CELULAR', b'Celular')])),
            ],
            options={
                'verbose_name': 'Tel\xe9fono',
                'verbose_name_plural': 'Tel\xe9fonos',
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido_materno',
            field=models.CharField(max_length=200, verbose_name=b'Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido_paterno',
            field=models.CharField(max_length=200, verbose_name=b'Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='curp',
            field=models.CharField(max_length=18, verbose_name=b'CURP o INE', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=250, verbose_name=b'Direccion', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=250, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name=b'Fecha de Nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=250, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observaciones',
            field=models.CharField(max_length=1000, verbose_name=b'Observaciones'),
        ),
        migrations.AddField(
            model_name='telefono',
            name='cliente',
            field=models.ForeignKey(related_name='telefono', verbose_name=b'Cliente', to='clientes.Cliente'),
        ),
        migrations.AlterUniqueTogether(
            name='telefono',
            unique_together=set([('cliente', 'telefono', 'tipo_telefono')]),
        ),
    ]
