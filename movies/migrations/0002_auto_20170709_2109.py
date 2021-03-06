# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de calificación de la película'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rate_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Veces que se ha calificado a la pelicula'),
        ),
    ]
