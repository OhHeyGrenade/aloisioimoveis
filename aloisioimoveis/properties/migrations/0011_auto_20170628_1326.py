# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_auto_20170617_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['order'], 'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
    ]
